#!/usr/bin/python3
"""Fabric script that generates a .tgz
archive from the contents of the web_static
folder of your AirBnB Clone repo,
using the function do_pack and Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy"""
from fabric.api import *
import os
from fabric.api import local
from datetime import datetime


env.hosts = ['<54.236.25.73 web-01>', '52.91.178.190 web-02']
env.user = "ubuntu"


def do_pack():
    """function to generate .tgx archive"""
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        archive = "versions/web_static_{:s}.tgz".format(date)
        local("tar -cvzf {:s} web_static".format(archive))
        return archive
    except:
        return None


@task
def do_deploy(archive_path):
    """function to deploy archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    archive_filename = os.path.basename(archive_path)
    release_path = "/data/web_static/releases/{}/".format(archive_filename[:-4])
    try:
        put(archive_path, "/tmp/{:s}".format(archive_filename))
        run("mkdir -p {:s}".format(release_path))
        run("tar -xzf /tmp/{:s} -C {:s}".format(archive_filename, release_path))
        run("rm /tmp/{:s}".format(archive_filename))
        run("mv {:s}/web_static/* {:s}/".format(release_path, release_path))
        run("rm -rf {:s}/web_static".format(release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {:s} /data/web_static/current".format(release_path))
        print("New version deployed!")
        return True
    except:
        return False
