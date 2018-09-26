#!usr/bin/python
# -*- coding: utf-8 -*-
"""Webotron: Deploy websites to AWS using Boto3.

-Configure AWS S3 buckets
    -Create them
    -Set them up for static website hosting
    -Deploy local files to them
- Configure DNS with AWS Route 53self.
-Configure a Content Delivery Network and SSL with AWS and Cloudfront
"""

import boto3
import click

from bucket import BucketManager


session = boto3.Session(profile_name='lupinePedagogy')
bucket_manager = BucketManager(session)
# s3 = session.resource('s3')


@click.group()
def cli():
    """Webotron deploys websites to AWS."""
    pass


@cli.command('list-buckets')
def list_buckets():
    """List all s3 buckets."""
    for bucket in bucket_manager.all_buckets():
        print(bucket)


@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    """List objects in an S3 bucket, specified by user input provided when executing script."""
    # for object in s3.Bucket(bucket).objects.all():
    for object in bucket_manager.all_objects(bucket):
        print(object)


@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    """Create and Configure S3 Bucket specified by user."""
    s3_bucket = bucket_manager.init_bucket(bucket)
    bucket_manager.set_policy(s3_bucket)
    bucket_manager.configure_website(s3_bucket)



#define upload file function for use with "sync" command



@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')
def sync(pathname, bucket):
    """Sync contents of PATHNAME to BUCKET."""
    bucket_manager.sync(pathname, bucket)


if __name__ == '__main__':
    cli()
