import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class CleverTap:
    def __init__(self, account_id: str, passcode: str):
        self.headers = {
            'X-CleverTap-Account-Id': account_id,
            'X-CleverTap-Passcode': passcode,
            'Content-Type': 'application/json',
        }
        retry_strategy = Retry(
            total=3, status_forcelist=[429, 500, 503], backoff_factor=1
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session = requests.Session()
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        self.session = session

    def get_event_count(self, event_name: str, start_date: int, end_date: int) -> int:
        url = 'https://api.clevertap.com/1/counts/events.json'
        body = {
            'event_name': event_name,
            'from': start_date,
            'to': end_date
        }
        response = self.session.post(url, headers=self.headers, json=body)

        while response.json()['status'] == 'partial' and response.status_code == 200:
            response = self.session.get('{}?req_id={}'.format(url, response.json()['req_id']), headers=self.headers)
        return response.json().get('count')

    def get_event_data(self, event_name: str, data_date: int, cursor: str = None) -> list:
        url = 'https://api.clevertap.com/1/events.json'
        body = {
            'event_name': event_name,
            'from': data_date,
            'to': data_date
        }
        if cursor is None:    
            params = {
                'batch_size': 5000,
                'app': True,
                'profile': True
            }
            response = self.session.post(url, headers=self.headers, json=body, params=params)
            self.check_response(response)
            while response.json()['status'] != 'success' and response.status_code == 200:
                response = self.session.post(url, headers=self.headers, json=body, params=params)
                self.check_response(response)
            cursor = response.json().get('cursor')
            if cursor is None:
                return None, None

        response = self.session.post('{}?cursor={}'.format(url, cursor), headers=self.headers, json=body)
        self.check_response(response)
        while response.json()['status'] != 'success' and response.status_code == 200:
            response = self.session.post('{}?cursor={}'.format(url, cursor), headers=self.headers, json=body)
            self.check_response(response)

        if response.json().get('records') is None:
            return None, None
        return response.json().get('records'), response.json().get('next_cursor')

    def upload_event(self, data: list):
        url = 'https://api.clevertap.com/1/upload'
        body = {
            'd': data
        }
        self.session.post(url, headers=self.headers, json=body).json()

    def check_response(self, response):
        try:
            response.json()
        except Exception:
            print(response.text)
            print(response.status_code)
