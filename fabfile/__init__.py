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
        for cmd in commands:
            if use_sudo:
                sudo(cmd, user=env.deploy_user)
            else:
                run(cmd)


def tail():
    if env.executable == 'www':
        cmd = 'tail -f /var/log/messages | grep -e www1 -e www2'
        sudo(cmd)
    elif env.executable == 'zeoserver':
        cmd = 'tail -f /var/log/messages | grep -e zeoserver'
        sudo(cmd)


def pull():
    env.forward_agent = True
    _with_deploy_env(['git pull origin master'], use_sudo=False)


def stop():
    if env.executable == 'www':
        cmd = 'scl enable python27 "{}/bin/www1 stop"'.format(env.directory)
        sudo(cmd, user=env.deploy_user)
        cmd = 'scl enable python27 "{}/bin/www2 stop"'.format(env.directory)
        sudo(cmd, user=env.deploy_user)
    elif env.executable == 'zeoserver':
        cmd = 'scl enable python27 "{}/bin/zeoserver stop"'.format(env.directory)
        sudo(cmd, user=env.deploy_user)


def start():
    if env.executable == 'www':
        cmd = 'scl enable python27 "{}/bin/www1 start"'.format(env.directory)
        sudo(cmd, user=env.deploy_user)
        cmd = 'scl enable python27 "{}/bin/www2 start"'.format(env.directory)
        sudo(cmd, user=env.deploy_user)
    elif env.executable == 'zeoserver':
        cmd = 'scl enable python27 "{}/bin/zeoserver start"'.format(env.directory)
        sudo(cmd, user=env.deploy_user)


def restart():
    stop()
    start()


def restart_haproxy():
    sudo('killall haproxy', user=env.deploy_user)
    cmd = '{envdir}/bin/haproxy -D -f {envdir}/etc/haproxy.cfg'
    sudo(cmd.format(envdir=env.directory), user=env.deploy_user)


def restart_varnish():
    sudo('killall varnishd', user=env.deploy_user)
    cmd = '{envdir}/bin/varnish-script'
    sudo(cmd.format(envdir=env.directory), user=env.deploy_user)


def restart_memcached():
    cmd = '{envdir}/bin/memcached'.format(envdir=env.directory)
    for action in ('stop', 'start'):
        sudo('{} {}'.format(cmd, action), user=env.deploy_user)


def status():
    run('uptime')
    if env.executable == 'www':
        _with_deploy_env(['scl enable python27 "./bin/www1 status"',
                      'scl enable python27 "./bin/www2 status"',
                      'git log -1'])
    elif env.executable == 'zeoserver':
        _with_deploy_env(['scl enable python27 "./bin/zeoserver status"',
                      'git log -1'])


def buildout():
    cmd = 'scl enable python27 "{0}/bin/buildout -c {0}/{1}"'.format(
        env.directory, env.buildout_config)
    sudo(cmd, user=env.deploy_user)


def deploy():
    """
    Update code on the server and restart zope.
    """
    pull()
    stop()
    buildout()
    start()
