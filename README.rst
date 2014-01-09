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

There are two configurations available for running this buildout:
 1. one for developers (devel)
 2. one for production (deployment)

Prerequisites - What needs to be installed by sys admin
-------------------------------------------------------
This buildout is intended to run on Linux/Unix-based operating systems. The
buildout has been used and tested on Fedora, Debian, Ubuntu and Mac OS X.

Be sure that you have this software and libraries installed on the server
before you run buildout. These must be globally installed by the server
administrator.

 * python-2.7
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

This project also needs access to a MySQL database. Currently there is one that has the
data for the current BISE site. Either that database should be migrated to this server
or provide access from this servers to there.


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
pass the configuration argument for deployment::

   $ git clone git@github.com:eea/esdrt.plonebuildout.git
   $ cd esdrt.plonebuildout
   $ ./install.sh -c deployment.cfg
   $ ./bin/buildout -c deployment.cfg

The apache config for production is etc/apache-vh.conf

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
   @reboot cd /var/local/esdrt.plonebuildout && bin/zope-start


Database packing
------------------


Packing is a vital regular maintenance procedure The Plone database
does not automatically prune deleted content. You must periodically
pack the database to reclaim space.

Data.fs should be packed daily via a cron job::

   01 2 * * * /esdrt.plonebuildout/bin/zeopack


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

The Effort Sharing Decission Review Toolis free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Source code
===========

You can get the code for this project from:

 * https://github.com/eea/esdrt.plonebuildout (buildout)

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


