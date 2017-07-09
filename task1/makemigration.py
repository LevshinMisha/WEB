#!/usr/bin/env python
from manage import manage_args

if __name__ == "__main__":
    manage_args([['', 'makemigrations'], ['', 'migrate']])