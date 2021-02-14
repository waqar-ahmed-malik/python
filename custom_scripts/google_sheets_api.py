import requests
import logging


class GoogleSheet:
    def __init__(self, client_id: str, client_secret: str, refresh_token: str):
        self.client_id = client_id
        self.client_id = client_secret
        self.client_id = refresh_token

    def get_access_token(self) -> str:
        request_data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': self.refresh_token,
            'grant_type': 'refresh_token'
        }

        endpoint = 'https://www.googleapis.com/oauth2/v4/token'
        token_data = requests.post(endpoint, data=request_data).json()
        return "Bearer {}".format(token_data['access_token'])

    def get_google_spreadsheet_id(self, spreadsheet_name: str) -> str:
        mime_type = 'application/vnd.google-apps.spreadsheet'
        endpoint = 'https://www.googleapis.com/drive/v3/files'
        headers = {
            'Authorization': self.get_access_token()
        }
        response = requests.get(endpoint, headers=headers).json()
        for file in response['files']:
            if file['name'] == spreadsheet_name:
                if file['mimeType'] == mime_type:
                    return file['id']
        return None

    def read_data_from_google_spreadsheet(self, spreadsheet_name: str, sheet_name: str) -> list:
        spreadsheet_id = self.get_google_spreadsheet_id(spreadsheet_name)
        data = list()
        endpoint = "https://sheets.googleapis.com/v4/spreadsheets/{}/values/{}!A:Z".format(spreadsheet_id, sheet_name)
        headers = {
            "Authorization": self.get_access_token()
        }
        response = requests.get(endpoint, headers=headers).json()
        field_names = response['values'][0]
        for i in range(len(response['values'])):
            if i == 0:
                continue
            else:
                data.append(dict(zip(field_names, response['values'][i])))
        logging.info("Data Read successfully from Google sheets.")
        return data

    def clear_spreadsheet(self, spreadsheet_name: str, sheet_name: str):
        spreadsheet_id = self.get_google_spreadsheet_id(spreadsheet_name)
        endpoint = "https://sheets.googleapis.com/v4/spreadsheets/{}/values/{}!A:Z:clear".format(spreadsheet_id, sheet_name)
        headers = {
            "Authorization": self.get_access_token()
        }
        requests.post(endpoint, headers=headers)

    def write_data_into_spreadsheet(self, spreadsheet_name: str, sheet_name: str, data_list: list):
        spreadsheet_id = self.get_google_spreadsheet_id(spreadsheet_name)
        endpoint = "https://sheets.googleapis.com/v4/spreadsheets/{}/values/{}!A:Z".format(spreadsheet_id, sheet_name)
        params = {
            'valueInputOption': 'USER_ENTERED'
        }
        headers = {
            "Authorization": self.get_access_token()
        }
        body = {
            "range": "{}!A:Z".format(sheet_name),
            "majorDimension": "ROWS",
            "values": data_list
        }
        requests.put(endpoint, headers=headers, params=params, json=body)
