#!/usr/bin/python3
''' Distribute an archive to web servers using the function do_deploy '''
from datetime import datetime
from fabric.api import env, put, run
import os

env.hosts = ['54.90.40.0', '54.90.23.41']
env.user = 'ubuntu'


def do_deploy(archive_path):
    ''' Deploy the static files to the host servers
    Args:
        archive_path (str): The path to the archived static files
    '''
    if not os.path.exists(archive_path):
        return False
    try:
        file_name = os.path.basename(archive_path)
        dir_name = file_name.replace('.tgz', '')
        releases_path = '/data/web_static/releases/{}/'.format(dir_name)
        tmp_path = '/tmp/' + file_name

        put(archive_path, tmp_path)
        run('mkdir -p ' + releases_path)
        run('tar -xzf {} -C {}'.format(tmp_path, releases_path))
        run('rm ' + tmp_path)
        run('mv {}web_static/* {}'.format(releases_path, releases_path))
        run('rm -rf {}web_static'.format(releases_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(releases_path))
        print('New version deployed!')
        return True
    except Exception:
        return False
