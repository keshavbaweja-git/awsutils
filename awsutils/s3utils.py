import click
import boto3
from botocore.exceptions import ClientError

s3 = boto3.resource('s3')


@click.command()
@click.option('--bucket_name', help='bucket name')
def s3_delete_bucket(bucket_name):
    bucket = s3.Bucket(bucket_name)
    if not bucket_exists(bucket):
        print("Bucket %s does not exist" % (bucket_name))
        return
    print("Deleting bucket %s" % (bucket_name))
    bucket.object_versions.all().delete()
    bucket.delete()


def bucket_exists(bucket):
    if bucket.creation_date:
        return True
    else:
        return False
