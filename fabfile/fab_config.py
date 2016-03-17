import ConfigParser
import os
from fabric.api import env


def enviroment(location):
    config = ConfigParser.RawConfigParser()
    local_path = os.path.dirname(__file__)
    config.read(os.path.join(local_path, 'env.ini'))
    env.update(config.items(section=location))
    try:
        hosts = config.get(location, 'hosts')
        env.hosts = hosts.split()
    except ConfigParser.NoOptionError:
        pass


def plone():
    """
    Settings for the plone server.
    """
    enviroment('plone')


def staging():
    plone()
    enviroment('staging')


def dog4():
    plone()
    enviroment('dog4')


def dog5():
    plone()
    enviroment('dog5')


def dog6():
    plone()
    enviroment('dog6')


def dog7():
    plone()
    enviroment('dog7')


def dog8():
    plone()
    enviroment('dog8')


def dog9():
    plone()
    enviroment('dog9')


def dog10():
    plone()
    enviroment('dog10')


def dog11():
    plone()
    enviroment('dog11')


def dog12():
    plone()
    enviroment('dog12')


def dog13():
    plone()
    enviroment('dog13')


def dogs():
    plone()
    enviroment('dogs')


def all_except_dog4():
    plone()
    enviroment('all_except_dog4')


def webserver():
    """
    Settings for the webserver.
    """
    enviroment('webserver')


def impala():
    webserver()


def zeo():
    """
    Settings for the zeo.
    """
    enviroment('zeo')


def bongo():
    zeo()
