#!/usr/bin/env python3
"""
Django command-line utility for administrative tasks.
"""

from __future__ import annotations

import os
import sys


def configure_settings() -> None:
    """
    Configure the default Django settings module.
    """
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "RootDjangoProject.settings",
    )


def run_cli() -> None:
    """
    Execute Django management commands from the command line.
    """
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django could not be imported. Ensure it is installed and "
            "available on your PYTHONPATH, and that your virtual environment "
            "is activated."
        ) from exc

    execute_from_command_line(sys.argv)


def main() -> None:
    configure_settings()
    run_cli()


if __name__ == "__main__":
    main()
