"""
Fabric script for deploying Plone consistently.
"""

from __future__ import with_statement
from fabric.api import *


try:
    from fab_config import *
except:
    pass


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
    command1 = 'scl enable python27 "/var/local/esd/esdrt.buildout/bin/www1 stop"'
    command2 = 'scl enable python27 "/var/local/esd/esdrt.buildout/bin/www2 stop"'
    sudo(command1, user=env.deploy_user)
    sudo(command2, user=env.deploy_user)


def start():
    """
    Start up the instance and zeo.
    """
    command1 = 'scl enable python27 "/var/local/esd/esdrt.buildout/bin/www1 start"'
    command2 = 'scl enable python27 "/var/local/esd/esdrt.buildout/bin/www2 start"'
    sudo(command1, user=env.deploy_user)
    sudo(command2, user=env.deploy_user)


def restart():
    """
    Restart just the zope instance, not the zeo.
    """
    command1 = 'scl enable python27 "/var/local/esd/esdrt.buildout/bin/www1 restart"'
    command2 = 'scl enable python27 "/var/local/esd/esdrt.buildout/bin/www2 restart"'
    sudo(command1, user=env.deploy_user)
    sudo(command2, user=env.deploy_user)


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
    command = 'scl enable python27 "/var/local/esd/esdrt.buildout/bin/buildout -c %s -vv"' % env.buildout_config
    sudo(command, user=env.deploy_user)


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
