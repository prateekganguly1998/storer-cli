import click 
from google_storage_util import create_or_get_bucket, store_files
import os

@click.command()
@click.option('--file', help="Enter the path of the file", required=True, prompt= "File path please")
def store(file):
    '''
    This will store the file/folder into a Google storage bucket. 
    '''
    bucket = create_or_get_bucket()
    #checks if path is a file/
    isFile = os.path.isfile(file)
    isDirectory = os.path.isdir(file)
    if isDirectory:
        files = (os.listdir(file))
        for f in files: 
            blob = bucket.blob(f"documents/{file}/{f}")
            store_files(files=[os.path.abspath(f"{file}/{f}")],blob=blob)
    elif isFile:
        blob = bucket.blob(f"documents/{file}")
        print(blob)
        store_files(files=[file],blob=blob)