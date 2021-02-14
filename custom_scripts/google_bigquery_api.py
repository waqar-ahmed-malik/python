from google.cloud import bigquery
from google.cloud.exceptions import NotFound
import os
import logging


# Set Logging Level
logging.getLogger().setLevel(logging.INFO)

class BigQuery:
    def __init__(self, service_account_key_file_path: str):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_account_key_file_path
        self.client = bigquery.Client()

    def check_if_dataset_exists(self, client, dataset_name: str) -> bool:
        try:
            self.client.get_dataset(dataset_name)
            return True
        except NotFound:
            return False

    def check_if_table_exists(self, table_id: str) -> bool:
        try:
            self.client.get_table(table_id)
            return True
        except NotFound:
            return False

    def list_datasets(self) -> list:
        datasets = list(self.client.list_datasets())
        return datasets

    def create_dataset(self, dataset_name: str, location: str):
        dataset = bigquery.Dataset(dataset_name)
        dataset.location = location
        dataset = self.client.create_dataset(dataset, timeout=30)
        return dataset

    def delete_dataset(self, dataset_name: str):
        self.client.delete_dataset(dataset_name, delete_contents=True, not_found_ok=True)

    def list_tables(self, dataset_name: str) -> list:
        dataset = self.client.get_dataset(dataset_name)
        return list(self.client.list_tables(dataset))

    def load_local_csv(self, table_id: str, local_file_path: str):
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,
            autodetect=True,
        )
        with open(local_file_path, "rb") as source_file:
            job = self.client.load_table_from_file(source_file, table_id, job_config=job_config)
        job.result()

    def load_csv_from_uri(self, table_id: str, uri: str):
        job_config = bigquery.LoadJobConfig(
            autodetect=True,
            skip_leading_rows=1,
            source_format=bigquery.SourceFormat.CSV,
        )
        # uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"

        load_job = self.client.load_table_from_uri(uri, table_id, job_config=job_config)
        load_job.result()

    def insert_rows(self, table_id: str, rows: list):
        table = self.client.get_table(table_id)
        self.client.insert_rows(table, rows) 

    def add_column_to_table(self, table_id: str, column_name: str, column_type: str):
        table = self.client.get_table(table_id)
        original_schema = table.schema
        new_schema = original_schema[:]
        new_schema.append(bigquery.SchemaField("phone", "STRING"))
        table.schema = new_schema
        table = self.client.update_table(table, ["schema"])

    def copy_table(self, source_table_id: str, destination_table_id: str):
        job = self.client.copy_table(source_table_id, destination_table_id)
        job.result()

    def extract_to_gcs(self, bucket_name: str, blob_path: str, table_id: str, location: str):
        destination_uri = "gs://{}/{}".format(bucket_name, blob_path)
        extract_job = self.client.extract_table(table_id, destination_uri, location=location)
        extract_job.result()

    def delete_table(self, table_id):
        self.client.delete_table(table_id, not_found_ok=True)

    def restore_table(self, deleted_table_id: str, recovered_table_id: str, snapshot_epoch: int, location: str):
        # snapshot epoch is in milli seconds.
        snapshot_table_id = "{}@{}".format(deleted_table_id, snapshot_epoch)
        job = self.client.copy_table(snapshot_table_id, recovered_table_id, location=location)
        job.result()
    
    def run_bigquery_query(query: str) -> list:
        client = bigquery.Client()
        query_job = client.query(query)
        return [dict(row) for row in query_job.result()]

    def get_table_schema(dataset_id: str, table_id: str) -> list:
        bq_client = bigquery.Client()
        dataset_ref = bq_client.dataset(dataset_id)
        table_ref = dataset_ref.table(table_id)
        table = bq_client.get_table(table_ref)
        schema = []
        for field in table.schema:
            schema_field = {
                'name': field.name,
                'field_type': field.field_type,
                'is_nullable': field.is_nullable,
                'description': field.description
            }
            schema.append(schema_field)
        return schema
