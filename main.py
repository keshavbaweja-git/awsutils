import click
from awsutils.s3utils import s3_delete_bucket


@click.group()
def cli():
    pass


cli.add_command(s3_delete_bucket)

if __name__ == '__main__':
    cli()
