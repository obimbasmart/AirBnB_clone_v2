#!/usr/bin/python3
"""generate .tgz archive from web_static folder"""

from datetime import datetime
from fabric.api import run, env, local


def do_pack():
    """generate .tgz archive"""
    now = datetime.now()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second
    )
    path_to_archive = 'web_static'
    # create version directory
    local("sudo mkdir -p versions")
    local(f"tar -czvf {archive_name} {path_to_archive}")
    local(f"sudo mv {archive_name} versions")
    return f"version/{archive_name}"
