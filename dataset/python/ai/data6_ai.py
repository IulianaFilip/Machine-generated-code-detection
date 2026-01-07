from __future__ import annotations

import threading
from typing import Dict, List, Tuple

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

from models import StateResults
from states import STATES


class PyElectionApp:
    def __init__(self) -> None:
        self.refreshing: bool = False
        self.active_tasks: List[int] = []

        self._load_ui()
        self._init_models()

    def _load_ui(self) -> None:
        self.builder = Gtk.Builder()
        self.builder.add_from_file("pyelection.glade")
        self.builder.connect_signals(self)

        self.window: Gtk.Window = self.builder.get_object("mainWindow")
        self.window.show_all()

        self.progress = self.builder.get_object("updateBar")

    def _init_models(self) -> None:
        self.state_store = Gtk.ListStore(object, str, str, int, str)
        self.result_store = Gtk.ListStore(str, int, int)
        self.overall_store = Gtk.ListStore(str, int)

    def on_party_changed(self, widget) -> None:
        party = "D" if widget.get_active_text() == "Democrats" else "R"
        self._reset()
        self._run_idle(self._load_states(party))

    def _load_states(self, party: str):
        self.refreshing = True
        total = len(STATES)

        for index, (abbr, name) in enumerate(STATES, start=1):
            state = StateResults(abbr, name, party)
            self.state_store.append(state.get_list())

            self._update_progress(index, total)
            yield True

        self.refreshing = False
        yield False

    def _update_progress(self, current: int, total: int) -> None:
        fraction = current / total
        self.progress.set_fraction(fraction)
        self.progress.set_text(f"Updated {current}/{total} states")

    def _run_idle(self, generator) -> None:
        task_id = GLib.idle_add(lambda: next(generator, False))
        self.active_tasks.append(task_id)

    def on_quit(self, *args) -> None:
        Gtk.main_quit()


def main() -> None:
    app = PyElectionApp()
    Gtk.main()


if __name__ == "__main__":
    main()
