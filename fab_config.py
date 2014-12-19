"""
Fabric settings for hosts.
"""

from fabric.api import env

def plone():
    """
    Settings for the plone server.
    """

    # If your buildout file for QA is qa.cfg, the following line is correct:
    env.buildout_config = 'deployment-zope.cfg'

    # A list of hostnames to deploy on. The following will try to connect to

    env.gateway = 'larreategi@silverfish.eea.europa.eu'
    env.hosts = []

    # The deploy user. Most deploy commands will be run as this user.
    env.deploy_user = 'zope'

    # The root of your Plone instance.
    env.directory = '/var/local/esd/esdrt.buildout'


def dog1():
    plone()
    env.hosts = ['larreategi@dog1.eea.europa.eu']


def dog2():
    plone()
    env.hosts = ['larreategi@dog2.eea.europa.eu']


def dog3():
    plone()
    env.hosts = ['larreategi@dog3.eea.europa.eu']


def webserver():
    """
    Settings for the webserver.
    """

    # If your buildout file for QA is qa.cfg, the following line is correct:
    env.buildout_config = 'deployment-webserver.cfg'

    # A list of hostnames to deploy on. The following will try to connect to
    # myqaserver.mysite.com as your username:
    env.gateway = 'larreategi@silverfish.eea.europa.eu'
    env.hosts = ['larreategi@impala.eea.europa.eu']

    # The deploy user. Most deploy commands will be run as this user.
    env.deploy_user = 'zope'

    # The root of your Plone instance.
    env.directory = '/var/local/esd/esdrt.buildout'


def impala():
    webserver()


def zeo():
    """
    Settings for the zeo.
    """

    # If your buildout file for QA is qa.cfg, the following line is correct:
    env.buildout_config = 'deployment-zeo.cfg'

    # A list of hostnames to deploy on. The following will try to connect to
    # myqaserver.mysite.com as your username:
    env.gateway = 'larreategi@silverfish.eea.europa.eu'
    env.hosts = ['larreategi@bongo.eea.europa.eu']

    # The deploy user. Most deploy commands will be run as this user.
    env.deploy_user = 'zope'

    # The root of your Plone instance.
    env.directory = '/var/local/esd/esdrt.buildout'


def bongo():
    zeo()
