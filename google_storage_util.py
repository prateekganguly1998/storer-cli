# Imports the Google Cloud client library
from google.cloud import storage
import os
# Instantiates a client
storage_client = storage.Client()
import glob

# The name for the new bucket
bucket_name = "custom-storage-cli"
def create_or_get_bucket():
    # Creates the new bucket
    try:
        bucket = storage_client.create_bucket(bucket_name)
        print("Bucket {} created.".format(bucket.name))
    except:
        bucket = storage_client.get_bucket('custom-storage-cli')
        print(f"Bucket already exists by: {bucket.name}")
    return bucket

def store_files(files, blob):

    blob.upload_from_filename(files)
    print(f'Done uploading: {files}')

def upload_file(local_path,bucket, gcs_path):
    for local_file in glob.glob(local_path + '/**'):
            if not os.path.isfile(local_file):
                upload_file(local_file,bucket, gcs_path + "/" + os.path.basename(local_file))
            else:
                remote_path = os.path.join(gcs_path, local_file[1 + len(local_path):])
                blob = bucket.blob(remote_path)
                store_files(files=local_file, blob=blob)
