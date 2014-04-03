====================================================
Plone 4 buildout for ESD Review Tool
====================================================

.. contents ::

Buildout is a tool for easily creating identical development or production
environments. This tool gives you the right versions of Zope, Plone products
and python libraries to ensure that every installation gets exactly the same
configuration.

Everything is installed in a local folder. This prevents conflicts with
already existing python and zope packages. Nothing other than this folder
is touched, so the user doesn't need any special priviliges.

There are several configurations available for running this buildout:
 1. one for developers (development.cfg)
 2. on for the demoserver in BM (demoserver.cfg)
 3. 3 files for production environment (deployment-xxxx.cfg):
   1. For webserver (deployment-webserver.cfg at impala.eea.europa.eu)
   2. Zope instances (deployment-zope.cfg at dog{1,2,3}.eea.europa.eu)
   3. Zeo server (deployment-zeo.cfg at bongo.eea.europa.eu)

Prerequisites - What needs to be installed by sys admin
-------------------------------------------------------
This buildout is intended to run on Linux/Unix-based operating systems. The
buildout has been used and tested on Fedora, Debian, Ubuntu and Mac OS X.

Be sure that you have this software and libraries installed on the server
before you run buildout. These must be globally installed by the server
administrator.

 * python-2.6
 * python-dev (Debian/Ubuntu) / python-devel (RedHat/CentOS)
 * wget
 * lynx
 * poppler-utils (for pdftotext etc)
 * tar
 * gcc
 * make
 * libc6-dev (Debian/Ubuntu) / glibc-devel (RedHat/CentOS)
 * libxml2-devel
 * libxslt-devel
 * libcrypto
 * libsvn-dev and libaprutil1-dev (on Debian/Ubuntu)
 * apr-util-devel and subversion-devel (on RedHat/CentOS)
 * cyrus-sasl-devel (on RedHat/CentOS) or libsasl2-dev (on Debian/Ubuntu) as OpenLDAP dependency
 * wv (used to index Word documents) <http://wvware.sourceforge.net/> (can be installed after Plone install)
 * graphiz, graphiz-devel and graphiz-gd (read more under eea.relations)
 * xpdf and pdftk (read more under eea.converter)
 * ImageMagick ver 6.3.7+ (read more under eea.converter)
 * git
 * libcurl3-dev (Debian/Ubuntu) / curl-devel (RedHat/CentOS)
 * libbz2-dev (Debian/Ubuntu) / libbzip2-devel (RedHat/CentOS)
 * libmysqlclient18 and libmysqlclient-dev (Debian/Ubuntu) / libmysqlclient and libmysqlclient-devel (RedHat/CentOS)

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

=================  ===================  =============================
Debian/Ubuntu      CentOS               dependency for
=================  ===================  =============================
python 2.6         python 2.6           buildout
python-dev         python-devel         buildout
wget               wget                 buildout
lynx               lynx                 buildout
tar                tar                  buildout
gcc                gcc                  buildout
git > 1.8.3        git > 1.8.3          buildout
libc6-dev          glibc-devel          buildout
libxml2-dev        libxml2-devel        buildout
libxslt-dev        libxslt-devel        buildout
libsvn-dev         subversion-devel     buildout
libaprutil1-dev    apr-util-devel       buildout
wv                 wv                   http://wvware.sourceforge.net
poppler-utils      poppler-utils        pdftotext
libjpeg-dev        libjpeg-devel        Pillow
libsasl2-dev       cyrus-sasl-devel     OpenLDAP
readline-dev       readline-devel       buildout
build-essential    make                 buildout
libz-dev           which                buildout
libssl-dev         openssl-devel        buildout
--                 patch                buildout
--                 gcc-c++              buildout
=================  ===================  =============================

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

   $ git clone git@github.com:eea/esdrt.plonebuildout.git
   $ cd esdrt.plonebuildout
   $ ./install.sh -c development.cfg
   $ ./bin/buildout -c development.cfg

This first three steps only have to be done the first time you use this
buildout. When you later want to update the site because people have committed
changes you do::

   $ cd esdrt.plonebuildout
   $ git pull origin master
   $ ./bin/develop rb

If you want to use a production database, put your Data.fs in var/filestorage/.

To start the site::

   $ ./bin/instance fg (or start)

To debug::

   $ ./bin/instance debug

Run buildout for production (deployment)
----------------------------------------

The above instructions are for developers.
When running buildout in a production environment one should
pass the configuration argument for deployment of the current machine.

For the webserver::

   $ git clone git@github.com:eea/esdrt.plonebuildout.git
   $ cd esdrt.plonebuildout
   $ ./install.sh -c deployment-webserver.cfg
   $ ./bin/buildout -c deployment.webserver.cfg

For the webserver::

   $ git clone git@github.com:eea/esdrt.plonebuildout.git
   $ cd esdrt.plonebuildout
   $ ./install.sh -c deployment-webserver.cfg
   $ ./bin/buildout -c deployment.webserver.cfg

For each zope instance machine::

   $ git clone git@github.com:eea/esdrt.plonebuildout.git
   $ cd esdrt.plonebuildout
   $ ./install.sh -c deployment-zope.cfg
   $ ./bin/buildout -c deployment.zope.cfg

For the zeoserver::

   $ git clone git@github.com:eea/esdrt.plonebuildout.git
   $ cd esdrt.plonebuildout
   $ ./install.sh -c deployment-zeo.cfg
   $ ./bin/buildout -c deployment.zeo.cfg


The apache config is generated only in the webserver configuration
at /var/local/esd/etc/apache-vh.conf

Now buildout will use the production configuration and install ldap product
and other zope/plone products that are not used during web development.

The deployment buildout is based on the ZEO client and server. It installs
several zope instances, one zeo server and one debug instance.

To run the debug instance use::

   $ ./bin/instance fg


Cron jobs to be setup on production and development
---------------------------------------------------

On production::

   $ crontab -e -u zope
   @reboot cd /var/local/esd/esdrt.plonebuildout && bin/zope-start


Database packing
------------------


Packing is a vital regular maintenance procedure The Plone database
does not automatically prune deleted content. You must periodically
pack the database to reclaim space.

Data.fs should be packed daily via a cron job::

   01 2 * * * /var/local/esd/esdrt.plonebuildout/bin/zeopack


EEA deployment
--------------

The project name is `Effort Sharing Decission Review Tool` and it's based on
Zope/Plone framework.

Contacts
========

The project owners are:

 * Eduardas Kazakevicius DG CLIMA
 * Melanie Sporer EEA
 * Marie Jaegly EEA

Other people involved in this project are:

 * Alberto Telletxea (atelletxea at bilbomatica.es)
 * Mikel Larreategi (mlarreategi at codesyntax.com)

Copyright and license
=====================

The Initial Owner of the Original Code is European Environment Agency (EEA). All Rights Reserved.

The Effort Sharing Decission Review Tool is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Source code
===========

You can get the code for this project from:

 * https://github.com/eea/esdrt.plonebuildout (buildout)
 * https://github.com/eea/esdrt.theme (theme)
 * https://github.com/eea/esdrt.content (content-types and workflow)

Resources
=========

Hardware
~~~~~~~~

Minimum requirements:
 * 2048MB RAM
 * 2 CPU 1.8GHz or faster
 * 2GB hard disk space

Recommended:
 * 4096MB RAM
 * 4 CPU 2.4GHz or faster
 * 6GB hard disk space


Software
~~~~~~~~

Any recent Linux version.
apache2, memcached, any SMTP local server.


