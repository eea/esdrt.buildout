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

For the 5th step, at the momment just two developers from CodeSyntax have upload rights to PyPI, Mikel Larreategi (mlarreategi@codesyntax.com) and Aitzol Naberan (anaberan@codesyntax.com)

2. Install new version of the software
=======================================

#. After releasing new packages, buildout needs to be updated to install those new versions. Edit `versions.cfg` file and set the new version of the products. Then commit the changes to the git repository and push the changes to GitHub.

#. Then SSH to the relevant server (in normal conditions you will only need to update the Plone server, so ssh to dog{1,2,3}.eea.europa.eu using the credentials provided by EEA)

#. Update the buildout with the latest changes::

    $ cd /var/local/esd/esdrt.buildout/
    $ git fetch origin
    $ git merge origin/master

#. Re-run buildout::

    $ sudo -u zope ./bin/buildout -c deployment-zope.cfg -vv

#. Restart the Plone instances::

    $ sudo -u zope ./bin/www1 restart
    $ sudo -u zope ./bin/www2 restart
    $ sudo -u zope ./bin/www3 restart

    **NOTE**: during the development and testing stage of the tool, the only server that needs to be updated is dog1.eea.europa.eu. All services at dog2 and dog3 are stopped.

#. Run upgrade steps (if any): log into Plone, go to the Plone Control Panel and run the needed upgrades.



.. _`esdrt.content`: https://github.com/eea/esdrt.content
.. _`esdrt.theme`: https://github.com/eea/esdrt.theme
.. _PyPI: https://pypi.python.org
.. _`zest.releaser`: https://pypi.python.org/pypi/zest.releaser
