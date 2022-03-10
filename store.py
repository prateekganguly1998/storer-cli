import click 
from google_storage_util import create_or_get_bucket, upload_file


@click.command()
@click.option('--file', help="Enter the path of the file", required=True, prompt= "File path please")
def store(file):
    '''
    This will store the file/folder into a Google storage bucket. 
    Provide the relative or absolute path of your file/ folder and the structure will be replicated 
    while uplaoding to the storage account.
    '''
    # assert os.path.isdir(file)
    bucket = create_or_get_bucket()
    upload_file(file, bucket, "document")

