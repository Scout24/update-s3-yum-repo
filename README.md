update-s3-yum-repo
==================

Maintain a YUM Repository in a S3 bucket.

Usage
-----

- Create a S3 bucket
- Create a [s3cmd config file](http://s3tools.org/kb/item14.htm) in `/etc/update-s3-yum-repo.conf` with at least the access and secret keys, e.g.
```ini
[default]
access_key = TUOWAAA99023990001
secret_key = sd/ceP_vbb#eDDDK 
```
  The provided access and secret keys need to have at least List/Get/Put permissions on this S3 bucket

- Run `update-s3-yum-repo s3://bucket-name` to initialize the YUM repo
- Run `update-s3-yum-repo s3://bucket-name <RPM files ...>` to add RPM packages to the YUM repo

Installation
------------

Tested on RHEL6 (compatible) with EPEL attached.

- Checkout source from GitHub
- Run `make` to build a dist archive and RPMs in `dist/`
- Install the RPM, it will pull in all required dependencies
