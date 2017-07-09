#!/usr/bin/env python
from manage import manage_args
from project_settings import your_ip, port

if __name__ == "__main__":
    manage_args([['', 'runserver', your_ip + ':' + port]])