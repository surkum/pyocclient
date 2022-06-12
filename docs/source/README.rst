==================================
Python client library for nextCloud
==================================


This is a fork of https://github.com/owncloud/pyocclient to provide compatibility with nextCloud, 
this client will not maintain compatibility to ownCloud.

This pure python library makes it possible to connect to an nextCloud instance
and perform file, share and attribute operations.

Please note that this is **not** a sync client implementation but a library
that provides functions to abstract away HTTP calls for various nextCloud APIs.

See the `nextCloud homepage <http://nextcloud.org>`_ for more information about nextCloud.

Features
========


General information
-------------------

- retrieve information about nextCloud instance (e.g. version, host, URL, etc.)

Accessing files
---------------

- basic file operations like getting a directory listing, file upload/download, directory creation, etc
- read/write file contents from strings
- upload with chunking and mtime keeping
- upload whole directories
- directory download as zip
- access files from public links
- upload files to files drop link target

Sharing (OCS Share API)
-----------------------

- share a file/directory via public link
- share a file/directory with another user or group
- unshare a file/directory
- check if a file/directory is already shared
- get information about a shared resource
- update properties of a known share

Apps (OCS Provisioning API)
---------------------------

- enable/disable apps
- retrieve list of enabled apps

Users (OCS Provisioning API)
----------------------------

- create/delete users
- create/delete groups
- add/remove user from groups

App data
--------

- store app data as key/values using the privatedata OCS API

Requirements
============

- Python >= 2.7 or Python >= 3.5
- requests module (for making HTTP requests)

Installation
============

Automatic installation with pip:

.. code-block:: bash

    $ pip install git+https://github.com/surkum/pyncclient.git

Manual installation of development version with git:

.. code-block:: bash

    $ pip install requests
    $ git clone https://github.com/surkum/pyocclient.git
    $ cd pyocclient
    $ python setup.py install

Usage
=====

Example for uploading a file then sharing with link:

.. code-block:: python

    import nextcloud_client

    nc = nextcloud_client.Client('http://domain.tld/nextcloud')

    nc.login('user', 'password')

    nc.mkdir('testdir')

    nc.put_file('testdir/remotefile.txt', 'localfile.txt')

    link_info = nc.share_file_with_link('testdir/remotefile.txt')

    print(f"Here is your link: {link_info.get_link()}")

Example for uploading a file to a public shared folder:

.. code-block:: python

    import nextcloud_client

    public_link = 'http://domain.tld/nextcloud/A1B2C3D4'

    nc = nextcloud_client.Client.from_public_link(public_link)
    nc.drop_file('myfile.zip')


Example for downloading a file from a public shared folder with password:

.. code-block:: python

    import nextcloud_client

    public_link = 'http://domain.tld/nextcloud/A1B2C3D4'
    folder_password = 'secret'

    nc = nextcloud_client.Client.from_public_link(public_link, password=folder_password)
    nc.get_file('/sharedfile.zip', 'download/destination/sharedfile.zip')

Running the unit tests
======================

To run the unit tests, create a config file called "nextcloud_client/test/config.py".
There is a config file example called "nextcloud_client/test/config.py.sample". All the
information required is in that file. 
It should point to a running nextCloud instance to test against.

You might also need to install the unittest-data-provider package:

.. code-block:: bash

    $ pip install unittest-data-provider

Then run the script "runtests.sh":

.. code-block:: bash

    $ ./runtests.sh

Building the documentation
==========================

To build the documentation, you will need to install Sphinx and docutil.
Then run the following commands:

.. code-block:: bash

    $ sphinx-apidoc -e -f -o docs/source nextcloud_client/ nextcloud_client/test
    $ cd docs
    $ make html

You can then find the documentation inside of "doc/build/html".

