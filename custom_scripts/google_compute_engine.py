# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

import logging
from googleapiclient import discovery
import os


logging.getLogger().setLevel(logging.INFO)


class ComputeEngine:
    def __init__(self, service_account_key_file_path: str, project_id: str):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_account_key_file_path
        self.project_id = project_id

    def stop_vm(self, name: str, zone: str):
        service = discovery.build('compute', 'v1', cache_discovery=False)
        request = service.instances().stop(project=self.project_id, zone=zone, instance=name)
        request.execute()
        logging.info('VM {} Stopped Successfully in the {} zone'.format(name, zone))
    
    def start_vm(self, name: str, zone: str):
        logging.getLogger().setLevel(logging.INFO)
        service = discovery.build('compute', 'v1', cache_discovery=False)
        request = service.instances().start(project=self.project_id, zone=zone, instance=name)
        request.execute()
        logging.info('VM {} Started Successfully in the {} zone'.format(name, zone))