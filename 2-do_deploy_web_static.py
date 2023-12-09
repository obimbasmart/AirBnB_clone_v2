#!/usr/bin/python3
"""distributes an archive to  web servers"""

from fabric.api import run, env, put
import os
env.user = "ubuntu"
env.hosts = ["107.23.95.20", "3.90.81.224"]


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
