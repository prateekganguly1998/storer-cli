import click 
from google_storage_util import create_or_get_bucket, store_files
import os
import glob


@click.command()
@click.option('--file', help="Enter the path of the file", required=True, prompt= "File path please")
def store(file):
    '''
    This will store the file/folder into a Google storage bucket. 
    '''
    # assert os.path.isdir(file)
    bucket = create_or_get_bucket()
    upload_file(file, bucket, "document")

def upload_file(local_path,bucket, gcs_path):
    for local_file in glob.glob(local_path + '/**'):
            if not os.path.isfile(local_file):
                upload_file(local_file,bucket, gcs_path + "/" + os.path.basename(local_file))
            else:
                remote_path = os.path.join(gcs_path, local_file[1 + len(local_path):])
                blob = bucket.blob(remote_path)
                store_files(files=local_file, blob=blob)
