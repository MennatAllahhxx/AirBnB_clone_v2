#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive 
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """a method to generate .tgz archive"""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"versions/web_static_{date}.tgz"
    try:
        local(f"tar -cvzf {filename} web_static")
        return filename
    except Exception as e:
        return None
