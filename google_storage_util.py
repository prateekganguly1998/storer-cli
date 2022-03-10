# Imports the Google Cloud client library
from google.cloud import storage
# Instantiates a client
storage_client = storage.Client()

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