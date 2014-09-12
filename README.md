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
bucket_location = eu-west-1
host_base = s3-eu-west-1.amazonaws.com
host_bucket = %(bucket)s.s3-eu-west-1.amazonaws.com
website_endpoint = http://%(bucket)s.s3-website-%(location)s.amazonaws.com/
```
  The provided access and secret keys need to have at least List/Get/Put permissions on this S3 bucket. For performance reason you should also adjust s3cmd for your primary region.

- Run `update-s3-yum-repo s3://bucket-name` to initialize the YUM repo
- Run `update-s3-yum-repo s3://bucket-name <RPM files ...>` to add RPM packages to the YUM repo

Installation
------------

Tested on RHEL6 (compatible) with EPEL attached.

- Checkout source from GitHub
- Run `make` to build a dist archive and RPMs in `dist/`
- Install the RPM, it will pull in all required dependencies


If using the [yum repo server](https://github.com/immobilienscout24/yum-repo-server/) then `TARGET_REPO=<repo-name> make rpmrepo` builds and uploads in one step :-)

AWS Policy
----------

The user needs the following AWS Policy on the S3 bucket (maybe even less, did not have time to narrow it down)
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:ListBucket",
        "s3:ListBucketMultipartUploads",
        "s3:ListBucketVersions",
        "s3:ListMultipartUploadParts",
        "s3:GetBucketAcl",
        "s3:GetBucketCORS",
        "s3:GetBucketLocation",
        "s3:GetBucketLogging",
        "s3:GetBucketNotification",
        "s3:GetBucketPolicy",
        "s3:GetBucketRequestPayment",
        "s3:GetBucketTagging",
        "s3:GetBucketVersioning",
        "s3:GetBucketWebsite",
        "s3:GetLifecycleConfiguration"
      ],
      "Resource": "arn:aws:s3:::bucket-name"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:AbortMultipartUpload",
        "s3:DeleteObject",
        "s3:GetObject",
        "s3:GetObjectAcl",
        "s3:GetObjectTorrent",
        "s3:GetObjectVersion",
        "s3:GetObjectVersionAcl",
        "s3:GetObjectVersionTorrent",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::bucket-name/*"
      ]
    }
  ]
}
```
