import click
import boto3

s3 = boto3.resource('s3')


@click.command()
@click.option('--bucket_name', help='bucket name')
def s3_delete_bucket(bucket_name):
    print("Deleting s3 bucket %s" % (bucket_name))
    bucket = s3.Bucket(bucket_name)
    bucket.object_versions.all().delete()
    bucket.delete()
