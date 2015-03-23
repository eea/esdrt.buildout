"""
Fabric script for deploying Plone consistently.
"""

from __future__ import with_statement
from fabric.api import *


try:
    from fab_config import *
except:
    pass


def test():
    plone()
    with cd(env.directory):
        run('echo "test"')


def _with_deploy_env(commands=[], use_sudo=True):
    """
    Run a set of commands as the deploy user in the deploy directory.
    """
    with cd(env.directory):
        for command in commands:
            if use_sudo:
                sudo(command, user=env.deploy_user)
            else:
                run(command)


def touch():
    _with_deploy_env(['touch mikel2.txt'])


def tail():
    _with_deploy_env(['tail -f var/log/www1.log'], use_sudo=False)


def pull():
    """
    Do a git pull.
    """
    env.forward_agent = True
    _with_deploy_env(['git pull origin master'], use_sudo=False)


def stop():
    """
    Shutdown the instance and zeo.
    """
    _with_deploy_env(['./bin/www1 stop', './bin/www2 stop'])


def start():
    """
    Start up the instance and zeo.
    """
    _with_deploy_env(['./bin/www1 start', './bin/www2 start'])


def restart():
    """
    Restart just the zope instance, not the zeo.
    """
    _with_deploy_env(['./bin/www1 restart', './bin/www2 restart'])


def status():
    """
    Find out the running status of the server and deploy.
    """

    # General health of the server.
    run('uptime')

    # Deploy and running status
    _with_deploy_env(['./bin/www1 status',
                      './bin/www2 status',
                      'git log -1'])


def buildout():
    """
    Rerun buildout.
    """
    _with_deploy_env(['./bin/buildout -c %s -vv' % env.buildout_config])


def deploy():
    """
    Update code on the server and restart zope.
    """
    pull()
    stop()
    buildout()
    start()


def extra():
    """ Should normally just contain 'pass'. Useful for
        testing individual commands before integrating them into
        another function.
    """
    pass
