#!/usr/bin/python3
"""archive and distribute static
file to web servers"""

from fabric.api import run, env, put, local
from datetime import datetime
import os

env.user = "ubuntu"
env.hosts = ["107.23.95.20", "3.90.81.224"]
env.key_filename = "~/.ssh/id_rsa"


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
    return f"versions/{archive_name}"


def do_deploy(archive_path):
    """distribute archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    archive_path = os.path.basename(archive_path)
    print(archive_path)
    put(f"versions/{archive_path}", "/tmp")
    run(f'sudo mkdir -p /data/web_static/releases/{archive_path[:-4]}')
    run(f"sudo tar -xzvf /tmp/{archive_path} -C "
        f"/data/web_static/releases/{archive_path[:-4]}")
    run(f"sudo rm  /tmp/{archive_path}")
    run(f"sudo mv /data/web_static/releases/{archive_path[:-4]}/web_static/* "
        f"/data/web_static/releases/{archive_path[:-4]}")
    run(f"sudo rm -rf /data/web_static/current")
    run(
        f"sudo ln -sf /data/web_static/releases/{archive_path[:-4]} "
        f"/data/web_static/current")
    # restart servers
    run("sudo service nginx restart")
    return True


def deploy():
    """pack and deploy"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path=archive_path)
