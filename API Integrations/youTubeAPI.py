import requests
from googleAPI import get_access_token


def get_lifetime_channel_community(client_id: str, client_secret: str, refresh_token: str, channel_id: str) -> int:
    access_token = get_access_token(client_id, client_secret, refresh_token)
    headers = {
        'Authorization': 'Basic {}'.format(encoded_consumer_combination.decode('utf-8'))
    }
    endpoint = 'https://www.googleapis.com/youtube/v3/channels'
    params = {
        'id': channel_id,
        'part': 'statistics'
    }
    response = requests.get(endpoint, headers=headers, params=params).json()
    return response['items'][0]['statistics']['subscriberCount']
