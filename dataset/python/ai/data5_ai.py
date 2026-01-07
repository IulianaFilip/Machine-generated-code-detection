from __future__ import annotations

import datetime
import re
import time
from typing import Dict, List, Optional
from urllib.request import urlopen

from bs4 import BeautifulSoup

RESULT_URL = "http://politics.nytimes.com/election-guide/2008/results/states/{abbr}.html"


class StateResults:
    def __init__(self, abbr: str, name: str, party: str = "D") -> None:
        if party not in {"D", "R"}:
            raise ValueError("Party must be either 'D' or 'R'.")

        self.abbr = abbr
        self.name = name
        self.party = party
        self.url = RESULT_URL.format(abbr=abbr)

        self.candidates: List[Dict[str, int | str]] = []
        self.reporting: int = 0
        self.date: Optional[datetime.date] = None

        self.refresh()

    def __repr__(self) -> str:
        return f"<StateResults state={self.name}>"

    def refresh(self) -> None:
        page_content = urlopen(self.url).read()
        soup = BeautifulSoup(page_content, "html.parser")

        area, date_text = self._extract_area_and_date(soup)
        self.reporting = self._extract_reporting(area)
        self.candidates = self._extract_candidates(area)
        self.date = self._parse_date(date_text)

    def _extract_area_and_date(self, soup: BeautifulSoup):
        column = "a" if self.party == "D" else "b"

        area = soup.find(attrs={"class": f"subcolumn-{column} results"})
        date_area = soup.find(attrs={"class": f"subcolumn-{column}"})

        try:
            date_text = (
                date_area.find(attrs={"class": "minor_subcolumn-a"})
                .contents[1]
                .contents[0]
                .strip()
            )
        except Exception:
            date_text = None

        return area, date_text

    def _extract_reporting(self, area) -> int:
        try:
            text = area.find(attrs={"class": "footer-note"}).get_text()
            return int(text.split("%")[0].strip())
        except Exception:
            return 0

    def _extract_candidates(self, area) -> List[Dict[str, int | str]]:
        results = []

        try:
            candidates = area.find(
                attrs={"class": re.compile(r"^results")}
            ).find_all(attrs={"class": re.compile(r"^candidate")})

            for candidate in candidates:
                parent = candidate.parent
                children = parent.find_all(recursive=False)

                results.append(
                    {
                        "name": children[0].get_text(strip=True),
                        "votes": int(children[1].get_text(strip=True).replace(",", "")),
                        "delegates": int(children[3].get_text(strip=True))
                        if len(children) > 3
                        else 0,
                    }
                )
        except Exception:
            results.append(
                {"name": "No results yet", "votes": 0, "delegates": 0}
            )

        return results

    def _parse_date(self, date_text: Optional[str]) -> Optional[datetime.date]:
        if not date_text:
            return None

        try:
            parsed = time.strptime(date_text, "%B %d, %Y")
            return datetime.date(*parsed[:3])
        except Exception:
            return None

    @property
    def winner(self) -> Dict[str, int | str]:
        return max(
            self.candidates,
            key=lambda c: (c["delegates"], c["votes"]),
        )

    @property
    def date_text(self) -> str:
        return self.date.strftime("%m-%d-%Y") if self.date else "Future"

    def to_list(self) -> List:
        return [self, self.name, self.winner["name"], self.reporting, self.date_text]
