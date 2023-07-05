#!/usr/bin/python3
"""Fabric script that generates a .tgz
archive from the contents of the web_static
folder of your AirBnB Clone repo,
using the function do_pack"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """function to generate .tgx archive"""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = "versions/web_static_{:s}.tgz".format(date)
    try:
        local("tar -cvzf {:s} web_static".format(archive))
        return archive
    except:
        return None