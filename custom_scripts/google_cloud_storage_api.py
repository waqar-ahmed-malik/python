from google.cloud import storage
import os


class GCS:
    def __init__(self, service_account_key_file_path: str):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_account_key_file_path
        self.client = storage.Client()

    def upload_file(self, bucket_name: str, local_file_path: str, blob_path: str):
        bucket = self.client.bucket(bucket_name)
        blob = bucket.blob(blob_path)
        blob.upload_from_file(local_file_path)

    def upload_data(self, bucket_name: str, data: bytes, blob_path: str):
        bucket = self.client.bucket(bucket_name)
        blob = bucket.blob(blob_path)
        blob.upload_from_string(data)

    def list_blobs(self, bucket_name: str, blob_prefix: str, extension: str) -> list:
        bucket = self.client.bucket(bucket_name)
        return [blob.name for blob in bucket.list_blobs(prefix=blob_prefix) if blob.name.split('.')[-1] == extension]

    def download_blob_to_file(self, bucket_name: str, local_file_path: str, blob_path: str):
        bucket = self.client.bucket(bucket_name)
        blob = bucket.get_blob(blob_path)
        blob.download_to_filename(local_file_path)

    def download_blob_as_string(self, bucket_name: str, blob_path: str) -> str:
        bucket = self.client.bucket(bucket_name)
        blob = bucket.get_blob(blob_path)
        return blob.download_as_string()

    def download_blob_as_bytes(self, bucket_name: str, blob_path: str) -> bytes:
        bucket = self.client.bucket(bucket_name)
        blob = bucket.get_blob(blob_path)
        return blob.download_as_bytes()

    def clean_folder(self, folder_path: str, bucket: str):
        bucket = self.client.get_bucket(bucket)
        for blob in bucket.list_blobs(prefix=folder_path):
            blob.delete()

    def copy_blob(self, bucket_name, blob_name, new_bucket_name, new_blob_name):
        source_bucket = self.client.get_bucket(bucket_name)
        source_blob = source_bucket.blob(blob_name)
        destination_bucket = self.client.get_bucket(new_bucket_name)
        source_bucket.copy_blob(source_blob, destination_bucket, new_blob_name)
