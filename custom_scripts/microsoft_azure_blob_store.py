from azure.storage.blob import BlobServiceClient
import os
import requests


class BLOBStorage:
    def __init__(self, connection_string: str):
        self.blob_service_client = BlobServiceClient.from_connection_string(
            connection_string
        )

    def upload_blob(
        self, container_name: str, local_file_path: str, blob_path: str
    ):
        blob_client = self.blob_service_client.get_blob_client(
            container=container_name, blob=blob_path
        )
        with open(local_file_path, 'rb') as f:
            blob_client.upload_blob(f, max_concurrency=16)
            blob_client.set_standard_blob_tier('Archive')

    def list_blobs(self, container_name: str) -> list:
        container_client = self.blob_service_client.get_container_client(
            container_name
        )
        return [blob.name for blob in container_client.list_blobs()]

    def delete_blob(self, container_name: str, blob_path: str):
        pass
