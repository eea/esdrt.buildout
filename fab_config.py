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

    env.gateway = 'silverfish.eea.europa.eu'
    env.hosts = []

    # The deploy user. Most deploy commands will be run as this user.
    env.deploy_user = 'zope'

    # The root of your Plone instance.
    env.directory = '/var/local/esd/esdrt.buildout'


def staging():
    plone()
    env.hosts = ['dogsdev.eea.europa.eu']
    env.buildout_config = 'staging.cfg'


# def dog1():
#     plone()
#     env.hosts = ['dog1.eea.europa.eu']


# def dog2():
#     plone()
#     env.hosts = ['dog2.eea.europa.eu']


# def dog3():
#     plone()
#     env.hosts = ['dog3.eea.europa.eu']


def dog4():
    plone()
    env.hosts = [
        '10.50.4.34',
    ]


def dog5():
    plone()
    env.hosts = [
        '10.50.4.35',
    ]


def dog6():
    plone()
    env.hosts = [
        '10.50.4.36',
    ]


def dog7():
    plone()
    env.hosts = [
        '10.50.4.37',
    ]


def dog8():
    plone()
    env.hosts = [
        '10.50.4.38',
    ]


def dog9():
    plone()
    env.hosts = [
        '10.50.4.39',
    ]


def dogs():
    plone()
    env.hosts = [
        '10.50.4.34',
        '10.50.4.35',
        '10.50.4.36',
        '10.50.4.37',
        '10.50.4.38',
        '10.50.4.39',
        '10.50.4.43',
        '10.50.4.44',
        '10.50.4.45',
        '10.50.4.46',
    ]


def all_except_dog4():
    plone()
    env.hosts = [
        '10.50.4.35',
        '10.50.4.36',
        '10.50.4.37',
        '10.50.4.38',
        '10.50.4.39',
        '10.50.4.43',
        '10.50.4.44',
        '10.50.4.45',
        '10.50.4.46',
    ]


def webserver():
    """
    Settings for the webserver.
    """

    # If your buildout file for QA is qa.cfg, the following line is correct:
    env.buildout_config = 'deployment-webserver.cfg'

    # A list of hostnames to deploy on. The following will try to connect to
    # myqaserver.mysite.com as your username:
    env.gateway = 'silverfish.eea.europa.eu'
    env.hosts = ['impala.eea.europa.eu']

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
    env.gateway = 'silverfish.eea.europa.eu'
    env.hosts = ['bongo.eea.europa.eu']

    # The deploy user. Most deploy commands will be run as this user.
    env.deploy_user = 'zope'

    # The root of your Plone instance.
    env.directory = '/var/local/esd/esdrt.buildout'


def bongo():
    zeo()
