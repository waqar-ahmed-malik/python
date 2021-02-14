import requests
import logging
import json


# Set Logging Level
logging.getLogger().setLevel(logging.INFO)

class CustomException(Exception):
    pass


def upload_file(file_name: str, oauth_token: str) -> dict:
    url = 'https://slack.com/api/files.upload'
    files = {
        'file': (file_name, open(file_name, 'rb'))
    }
    body = {
        'token': oauth_token
    }
    response = requests.post(url, data=body, files=files)
    if response.status_code == 200:
        logging.info('File Uploaded Successfully.')
        return response.json()
    else:
        raise CustomException("Failed to upload File.")


def enable_file_for_public_sharing(file_object: dict, oauth_token:str):
    url = 'https://slack.com/api/files.sharedPublicURL'
    headers = {
        'Authorization': 'Bearer {}'.format(oauth_token)
    }
    params = {
        'file': file_object['file']['id']
    }

    response = requests.post(url, params=params, headers= headers)
    if response.status_code == 200:
        logging.info('File made Public Successfully.')
    else:
        raise CustomException("Failed to upload File.")


def send_image(image_file_path: str, oauth_token: str, bot_user_token: str, channel: str, message: str, thread_ts: str):
    file_object = upload_file(image_file_path, oauth_token)
    enable_file_for_public_sharing(file_object, oauth_token)
    team_id = file_object['file']['permalink_public'].split('/')[-1].split('-')[0]
    file_id = file_object['file']['id']
    file_name = file_object['file']['name']
    pub_secret = file_object['file']['permalink_public'].split('-')[-1]
    image_url = 'https://files.slack.com/files-pri/{}-{}/{}?pub_secret={}'.format(team_id, file_id, file_name, pub_secret)

    blocks_json = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": message
            }
        },
        {
            "type": "image",
            "image_url": image_url,
            "alt_text": "alternate_name"
        }
    ]
    url = 'https://slack.com/api/chat.postMessage'
    params = {
        'channel': channel,
        'token': bot_user_token,
        'blocks': json.dumps(blocks_json),
        'thread_ts': thread_ts,
        'reply_broadcast': False,
    }

    response = requests.post(url, params= params)
    if response.status_code == 200:
        if response.json().get('ts'):
            logging.info('Message With Image Sent Successfully.')
            return response.json()['ts']
        else:
            print(response.json())
            raise CustomException("Unable to send message.")
            
    else:
        raise CustomException("Unable to send message with Image.")


def send_text(bot_user_token: str, channel: str, message: str, thread_ts: str) -> str:
    url = 'https://slack.com/api/chat.postMessage'
    blocks_json = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": message
            }
        }
    ]
    params = {
        'channel': channel,
        'token': bot_user_token,
        'blocks': json.dumps(blocks_json),
        'thread_ts': thread_ts,
        'reply_broadcast': False
    }

    response = requests.post(url, params= params)
    if response.status_code == 200:
        if response.json().get('ts'):
            logging.info('Message Sent Successfully.')
            return response.json()['ts']
        else:
            print(response.json())
            raise CustomException("Unable to send message.")
    else:
        raise CustomException("Unable to send message.")

