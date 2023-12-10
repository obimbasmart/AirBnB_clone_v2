#!/usr/bin/python3
"""deletes out-of-date archives"""

import os
from fabric.api import local, env, run, get
from datetime import datetime

env.user = "ubuntu"
env.hosts = ['107.23.95.20', '3.90.81.224']


def pull_file():
    """pull filesnames from server"""
    remote_files = run("ls -t /data/web_static/releases/").stdout.split()
    return [file for file in remote_files if file != 'test']


def do_clean(number=0):
    """deletes out-of-date archives"""
    number = int(number)
    if number == 0:
        number = 1
    archives = sorted(os.listdir("versions/"),
                      key=lambda f:
                      datetime.strptime(f[11:-4], "%Y%m%d%H%M%S"),
                      reverse=True)
    [local(f"sudo rm versions/{file}") for file in archives[number:]]

    remote_filenames = pull_file()
    archives = sorted(remote_filenames, key=lambda f:
                      datetime.strptime(f[11:], "%Y%m%d%H%M%S"), reverse=True)
    [run(f"sudo rm -rf /data/web_static/releases/{dir}")
     for dir in archives[number:]]
