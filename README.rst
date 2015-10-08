====================================================
Plone 4 buildout for ESD Review Tool
====================================================

.. contents ::

ESD Review Tool
==================

The project name is `Effort Sharing Decission Review Tool` and it's based on
Zope/Plone framework.

Buildout is a tool for easily creating identical development or production
environments. This tool gives you the right versions of Zope, Plone products
and python libraries to ensure that every installation gets exactly the same
configuration.

This application is installed using buildout, and its buildout configuration is based on EEA-CPB [1]_. Everything is installed in a local folder. This prevents conflicts with already existing python and zope packages. Nothing other than this folder is touched, so the user doesn't need any special priviliges.

There are several configurations available for running this buildout:

 1. one for developers (development.cfg)
 2. on for the demoserver in BM (demoserver.cfg)
 3. 3 files for production environment (deployment-xxxx.cfg):

   1. For webserver (deployment-webserver.cfg at impala.eea.europa.eu)
   2. Zope instances (deployment-zope.cfg at dog{1,2,3}.eea.europa.eu)
   3. Zeo server (deployment-zeo.cfg at bongo.eea.europa.eu)


System requirements and preparation for ESD
===============================================

The ESD Review Tool is intended to run on Linux/Unix-based operating systems. The
buildout has been used and tested on *Debian*, *Ubuntu* for development and *CentOS 5* and *CentoOS 6* for production.

The below system libraries must be installed on the server before you run the buildout. These must be globally
installed by the server administrator.

For CentOS, the EPEL and RPMForge repositories need to be configured before installing
the packages, since some of them are not included in the base repo.

All installs will require the basic GNU build and archive tools: gcc, g++, gmake, gnu tar, gunzip, bunzip2 and patch.

On Debian/Ubuntu systems, this requirement will be taken care of by installing build-essential. On RPM systems (RedHat, Fedora, CentOS), you'll need the gcc-c++ (installs most everything needed as a dependency) and patch RPMs.

==========================  ===========================  =========================================
Debian/Ubuntu               CentOS                       dependency for
==========================  ===========================  =========================================
python 2.7                  python 2.7                   buildout
python-dev                  python-devel                 buildout
wget                        wget                         buildout
lynx                        lynx                         buildout
tar                         tar                          buildout
gcc                         gcc                          buildout
git > 1.8.3                 git > 1.8.3                  buildout
graphviz                    --                           eea.relations
graphviz-gd                 --                           eea.relations
graphviz-dev                graphviz-devel               eea.relations
ImageMagick > 6.3.7+        ImageMagick > 6.3.7+         eea.relations
libc6-dev                   glibc-devel                  buildout
libxml2-dev                 libxml2-devel                buildout
libxslt-dev                 libxslt-devel                buildout
libsvn-dev                  subversion-devel             buildout
libaprutil1-dev             apr-util-devel               buildout
wv                          wv                           http://wvware.sourceforge.net
poppler-utils               poppler-utils                pdftotext
libjpeg-dev                 libjpeg-turbo-devel          Pillow
libldap2-dev                openldap-devel               OpenLDAP
libsasl2-dev                cyrus-sasl-devel             OpenLDAP
readline-dev                readline-devel               buildout
build-essential             make                         buildout
libz-dev                    which                        buildout
libssl-dev                  openssl-devel                buildout
--                          patch                        buildout
--                          gcc-c++                      buildout
libcurl3-dev                curl-devel                   sparql-client and pycurl2
--                          redhat-lsb-core              init script
libmemcached                libmemcached                 memcached
libmemcached-dev>=0.40      libmemcached-devel>=0.40     memcached
zlib1g-dev                  zlib-devel                   memcached
libpq-dev                   postgresql94-devel           buildout/relstorage
==========================  ===========================  =========================================

Additional info to install git for CentOS::

$ wget http://puias.math.ias.edu/data/puias/computational/6/x86_64/git-1.8.3.1-1.sdl6.x86_64.rpm
$ wget http://puias.math.ias.edu/data/puias/computational/6/i386/perl-Git-1.8.3.1-1.sdl6.noarch.rpm
$ yum update  git-1.8.3.1-1.sdl6.x86_64.rpm perl-Git-1.8.3.1-1.sdl6.noarch.rpm


How to use this buildout
===========================

This section will describe the necessarily steps to run this buildout on the production
environment at the EEA

Note that all the commands stated bellow should not be executed root, your local user should be used instead.


Run buildout for development
----------------------------
The first time you want to use this buildout you first have to get
all software from github and then run a few commands::

   $ git clone git@github.com:eea/esdrt.buildout.git
   $ cd esdrt.buildout
   $ ./install.sh -c development.cfg
   $ ./bin/buildout -c development.cfg

This first three steps only have to be done the first time you use this
buildout. When you later want to update the site because people have committed
changes you do::

   $ cd esdrt.buildout
   $ git pull origin master
   $ ./bin/develop rb

If you want to use a production database, put your Data.fs in var/filestorage/.

To start the site::

   $ ./bin/instance fg (or start)

To debug::

   $ ./bin/instance debug


Preliminary work regarding the use of python2.7 as a Software Collection
-------------------------------------------------------------------------

The server setup uses `Software Collections`_ to install different versions of python. So to use python2.7 to run this buildout, you need first to enter a bash session which has python2.7 software collection enabled. To do so, run first this command::

    $ sudo -u zope scl enable python27 bash

From this moment on, the python2.7 will be available on the command-line and you will be logged-in as 'zope' user.


Run buildout for production (deployment)
----------------------------------------

Similar, as explained in the previous chapter, the first step on using the EEA-CPB is to setup the specific configuration needed. The list of all configurable settings (e.g. the number of Zope instances, port numbers, database location on file system etc.) can be found under deployment.cfg.

The [configuration] part contains a comprehensive list of configurable options. The values listed here are the buildout defaults. In order to override any of the settings just uncomment them.

Some preliminary preparations must be done by system administrators on the deployment server:

    a user and user group called 'zope' should be created having neccesary rights. The 'zope' is the default user, you can change this in the configuration section, just make sure the changes are consistent across the deployment.

    a project folder must be created under /var/local/esd/esdrt.buildout with group owner zope and 2775 (rwxrwxr-x) mode add under /etc/profile::

     if [ "`id -gn`" = "zope" ]; then
        umask 002
     fi

The first time you want to use the ESD buildout you have to run a few commands. Use the file needed by the server you are installing webserver, zope or zeo::

   $ cd /var/local/esd/
   $ git clone https://github.com/eea/esdrt.buildout
   $ cd esdrt.buildout
   $ ./install.sh
   $ ./bin/buildout -c deployment-webserver.cfg -vv
   $ ./bin/buildout -c deployment-zope.cfg -vv
   $ ./bin/buildout -c deployment-zeo.cfg -vv
   $ chmod -R g+rw .
   $ chmod -R g+x var/blobstorage-cache

Do not forget to run the last chmod commands to set the file permissions correctly.

Next time the buildout needs to be run (when updates need to be installed), you have to run buildout using sudo, as follows::

   $ cd /var/local/esd/esdrt.buildout
   $ git fetch origin
   $ git merge origin/master
   $ sudo -u zope scl enable python27 bash
   $ ./bin/buildout -c deployment-webserver.cfg -vv
   $ ./bin/buildout -c deployment-zope.cfg -vv
   $ ./bin/buildout -c deployment-zeo.cfg -vv

The apache config is generated only in the webserver configuration
at /var/local/esd/etc/apache-vh.conf

Now buildout will use the production configuration and install ldap product
and other zope/plone products that are not used during web development.

The deployment buildout is based on the ZEO client and server. It installs
several zope instances, one zeo server and one debug instance.

Running the application on production
-----------------------------------------

To run the debug instance use::

   $ ./bin/instance fg

Processes on production should be started with user zope using sudo, e.g::

   $ sudo -u zope ./bin/memcached start
   $ sudo -u zope ./bin/zeoserver start
   $ sudo -u zope ./bin/www1 start
   $ sudo -u zope ./bin/www2 start
   $ sudo -u zope ./bin/www3 start
   $ sudo -u zope ./bin/poundctl start

For the application stack to be restarted when server reboot, the system administrator should add under /etc/init.d the script from esdrt.buildout/etc/rc.d/restart-portal, e.g.::

   $ cd /var/local/esd/esdrt.buildout/etc/rc.d
   $ ln -s `pwd`/restart-portal /etc/init.d/restart-portal
   $ chkconfig --add restart-portal
   $ chkconfig restart-portal on
   $ service restart-portal start


Cron jobs to be setup on production and development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Database packing::


Packing is a vital regular maintenance procedure The Plone database
does not automatically prune deleted content. You must periodically
pack the database to reclaim space.

Data.fs should be packed daily via a cron job::

   01 2 * * * /var/local/esd/esdrt.buildout/bin/zeopack

Backup policy
~~~~~~~~~~~~~

The backup policy should be established with sistem administrators. Locations to be backuped, backup frequency and backup retention should be decided.

Logs
~~~~

ESD buildout for deployment will generate logs from ZEO, Zope, Pound and Apache. All this logs have a default location and a default size on disk allocated for each of them.

A ZEO server only maintains one log file, which records starts, stops and client connections. Unless you are having difficulties with ZEO client connections, this file is uninformative. It also typically grows very slowly — so slowly that you may never need to rotate it. In respect of this ZEO log files will not be rotated and the default location on disk will be:

    /var/local/esd/esdrt.buildout/var/log/zeoserver.log

Zope client logs are of much more interest and grow more rapidly. There are two kinds of client logs, and each of your clients will maintain both, access logs and event logs. By default the logs will be rotated once they rich 100Mb in size and 3 old log files will be kept. Zope clients will write the logs on disk under /var/local/esd/esdrt.buildout/var/log/, e.g.:

    /var/local/esd/esdrt.buildout/var/log/www1-Z2.log
    /var/local/esd/esdrt.buildout/var/log/www1.log

Logs generated by Pound will be created under /var/local/esd/esdrt.buildout/var/log/pound.log. This logs must be rotated using logrotate.

Logs generated by Apache will be created under /var/log/httpd/*.log.

Contacts
========

The project owners are:

 * Eduardas Kazakevicius DG CLIMA
 * Melanie Sporer EEA (Melanie.Sporer at eea.europa.eu)
 * Marie Jaegly EEA (Marie.Jaegly at eea.europa.eu)
 * Franz Daffner EEA (Franz.Daffner at eea.europa.eu)
 * Christian Xavier Prosperini (Christian.Prosperini at eea.europa.eu)

Other people involved in this project are:

 * Alberto Telletxea (atelletxea at bilbomatica.es)
 * Mikel Larreategi (mlarreategi at codesyntax.com)
 * Mikel Santamaria (msantamaria at codesyntax.com)


Copyright and license
=====================

The Initial Owner of the Original Code is European Environment Agency (EEA). All Rights Reserved.

The Effort Sharing Decission Review Tool is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Source code
===========

You can get the code for this project from:

 * https://github.com/eea/esdrt.buildout (buildout)
 * https://github.com/eea/esdrt.theme (theme)
 * https://github.com/eea/esdrt.content (content-types and workflow)

Resources
=========

Hardware
------------

Minimum requirements:
 * 2048MB RAM
 * 2 CPU 1.8GHz or faster
 * 2GB hard disk space

Recommended:
 * 4096MB RAM
 * 4 CPU 2.4GHz or faster
 * 6GB hard disk space


Software
-------------

Any recent Linux version.
apache2, memcached, any SMTP local server.

.. [1] EEA-CPB, common buildout for EEA deployments: https://github.com/eea/eea.plonebuildout.core
.. [2] Check EEA-CPB documentation for more information https://github.com/eea/eea.plonebuildout.core#step-3-eea-cpb-for-production
