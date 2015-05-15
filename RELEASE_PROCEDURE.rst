====================================================
Release procedure for ESD Review Tool
====================================================

This document explains the release procedure for the ESD Review Tool

ESD Review Tool is hosted on several virtual servers accross the EEA's services. The requirements are stated at the README.rst file.

This document will explain how to create new version of the software and upload it to the related servers.

1. Release new version of the software
========================================

We have developed 2 add-on products for the ESD Review Tool:

* `esdrt.content`_: content-type, workflow definition, and templates
* `esdrt.theme`_: styles and Plone template customizations

Both products are standard Plone add-on packages and its installation is handled by buildout.

When a new version of the software is prepared, the procedure to follow to update the production servers is as follows:

#. Test all changes on development environments and provide upgrade steps if needed. Commit all changes into the git repository.
#. Explain roughly the changes in the `docs/CHANGES.txt` file
#. Create a new tag at the git repository.
#. Create a release distribution using `python setup.py sdist`
#. Upload the release distribution to PyPI_
#. Update the version number at `setup.py` and `docs/CHANGES.txt`
#. Commit the changes into the git repository.

The tasks from 2 to 5 can be managed using a dedicated tool like `zest.releaser`_.

For the 5th step, these are the users that can create the releases on PyPI:

* Mikel Larreategi (mlarreategi@codesyntax.com)
* Aitzol Naberan (anaberan@codesyntax.com)
* Mikel Santamaria (msantamaria@bilbomatica.es)

2. Install the new version of the software
==========================================

#. After releasing new packages, buildout needs to be updated to install those new versions. Edit `versions.cfg` file and set the new version of the products. Then commit the changes to the git repository and push the changes to GitHub.

#. Then SSH to the relevant server (in normal conditions you will only need to update the Plone server, so ssh to dog{4,5,6,7,8,9}.eea.europa.eu using the credentials provided by EEA).

#. Update the buildout with the latest changes::

    $ cd /var/local/esd/esdrt.buildout/
    $ git fetch origin
    $ git merge origin/master

#. Re-run buildout::

    $ sudo -u zope scl enable python27 bash
    $ sudo -u zope ./bin/buildout -c deployment-zope.cfg -vv

#. Restart the Plone instances::

    $ sudo -u zope scl enable python27 bash
    $ sudo -u zope ./bin/www1 restart
    $ sudo -u zope ./bin/www2 restart
    $ sudo -u zope ./bin/www3 restart


#. Run upgrade steps (if any): log into Plone, go to the Plone Control Panel and run the needed upgrades.

3. Install the new version of the software using Fabric
=======================================================

Some fabric_ scripts are provided to ease the deployment on EEA servers. To achieve that you will need to have fabric_ installed or buildout run with fab.cfg or development.cfg files.

#. Do the deployment in just one server (dog4)::

    $ fab dog4 deploy -u username -p password

Use the username and password provided by EEA Sysadmins to log-in on the servers.

#. Check that the deploy was OK. This will show the last lines of the instance.log file and check that the service is running::

    $ fab dog4 tail -u username -p password

Look for a line like this one::

    out: 2015-02-15T10:00:50 INFO Zope Ready to handle requests

Exit pressing Ctrl-C.

#. If the deployment on dog4 was OK, deploy the update on the other servers::

    $ fab all_except_dog4 deploy -u username -p password -P

The last -P option will force fabric to run the deployment in parallel in all servers.







.. _`esdrt.content`: https://github.com/eea/esdrt.content
.. _`esdrt.theme`: https://github.com/eea/esdrt.theme
.. _PyPI: https://pypi.python.org
.. _`zest.releaser`: https://pypi.python.org/pypi/zest.releaser
.. _fabric: https://fabric.readthedocs.org/
