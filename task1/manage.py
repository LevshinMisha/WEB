#!/usr/bin/env python
import os
import sys
from project_settings import project_root


def manage_args(to_exec):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", project_root + ".settings")
    from django.core.management import execute_from_command_line
    for command in to_exec:
        execute_from_command_line(command)


if __name__ == "__main__":
    manage_args([sys.argv])
