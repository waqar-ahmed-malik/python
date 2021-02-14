import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import logging
import math


# Set Logging Level
logging.getLogger().setLevel(logging.INFO)

class Leadsquared:
    def __init__(self, access_key: str, secret_key: str):
        self.access_key = access_key
        self.secret_key = secret_key
        self.headers = {
            'Content-Type': 'application/json'
        }
        retry_strategy = Retry(total = 5, status_forcelist = [500], backoff_factor = 5)
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session = requests.Session()
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        self.session = session


    def get_users(self) -> list:
        endpoint = 'https://api-in21.leadsquared.com/v2/UserManagement.svc/Users.Get'
        params = {
            'accessKey': self.access_key,
            'secretKey': self.secret_key
        }
        users = self.session.get(endpoint, params= params).json()
        return users

    
    def get_tasks_by_serch_criteria(self, search_criteria: dict) -> list:
        endpoint = 'https://api-in21.leadsquared.com/v2/Task.svc/RetrieveAppointments/ByUserSearchCriteria'
        params = {
            'accessKey': self.access_key,
            'secretKey': self.secret_key
        }
        body = search_criteria
        body.__setitem__('Paging', {'PageIndex': 1, 'PageSize': 1000})
        tasks = []
        response = self.session.post(endpoint, params=params, json=body, headers=self.headers).json()
        tasks.extend(response['List'])
        logging.info('{} tasks has been extracted'.format(len(tasks)))
        while len(response['List']) != 0:
            body['Paging']['PageIndex'] += 1
            response = self.session.post(endpoint, params=params, json=body, headers=self.headers).json()
            tasks.extend(response['List'])
            logging.info('{} tasks has been extracted'.format(len(tasks)))
        return tasks

    
    def get_lead_details_by_ids(self, lead_ids: list, columns: str) -> dict:
        lead_details = {}
        url = 'https://api-in21.leadsquared.com/v2/LeadManagement.svc/Leads/Retrieve/ByIds'
        params = {
            'accessKey': self.access_key,
            'secretKey': self.secret_key
        }
        for i in range(math.ceil(len(lead_ids)/1000)):
            lead_batch_ids = lead_ids[i*1000:(i+1)*1000] if (i+1)*1000 <= len(lead_ids) else lead_ids[i*1000:]
            body = {
                "SearchParameters": {
                "LeadIds": lead_batch_ids
                },
                "Columns": {"Include_CSV": columns}
            }
            response = requests.post(url, json=body, headers=self.headers, params=params)
            if response.status_code != 200:
                print(response.json())
                print(response.status_code)
            if response.json()['RecordCount'] == 0:
                continue
            else:
                lead_details.update({lead['ProspectID']: lead for lead in response.json()["Leads"]})
            logging.info('Processed {} of {} leads'.format(len(lead_details), len(lead_ids)))
        return lead_details

    
    def get_activities_by_event_code(self, event_code: int, start_time: str, end_time: str) -> list:
        activities = []
        url = 'https://api-in21.leadsquared.com/v2/ProspectActivity.svc/CustomActivity/RetrieveByActivityEvent'
        params = {
            'accessKey': self.access_key,
            'secretKey': self.secret_key
        }
        body = {
            'Parameter': {
                'FromDate': start_time,
                'ToDate': end_time,
                'ActivityEvent': event_code,
                "IncludeCustomFields": 1
            },
            'Paging': {
                'PageIndex': 1,
                'PageSize': 1000
            },
            'Sorting': {
                'ColumnName': "CreatedOn",
                'Direction': 1
            }
        }
    
        while True:
            response = requests.post(url, json=body, headers=self.headers, params=params)
            if response.json()['RecordCount'] == 0:
                break
            activities.extend(response.json()['List'])
            logging.info('{} Activities has been extracted'.format(len(activities)))
            body['Paging']['PageIndex'] += 1
        return activities

    
    def get_activity_by_activity_id(self, activity_id: str):
        url = 'https://api-in21.leadsquared.com/v2/ProspectActivity.svc/GetActivityDetails'
        params = {
            'accessKey': self.access_key,
            'secretKey': self.secret_key,
            'activityId': activity_id
        }
        activity = requests.get(url, params= params).json()
        return activity
    

    def get_task_by_task_id(self, task_id: str):
        url = 'https://api-in21.leadsquared.com/v2/Task.svc/Retrieve.GetById'
        params = {
            'accessKey': self.access_key,
            'secretKey': self.secret_key,
            'id': task_id
        }
        task = requests.get(url, params= params).json()
        return task
        



