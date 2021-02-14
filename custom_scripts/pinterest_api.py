import requests


class Pinterest:
    def __init__(self, advertiser_id: str, access_token: str) -> None:
        self.advertiser_id = advertiser_id
        self.access_token = access_token

    def get_delivery_metrics(self, start_date: str, end_date: str):
        url = "https://api.pinterest.com/ads/v3/reports/async/{}/delivery_metrics/".format(self.advertiser_id)
        payload = 'click_window_days=60&conversion_report_time=AD_EVENT&data_source=OFFLINE&start_date={}&end_date={}&engagement_window_days=60&entity_fields=AD_GROUP_ID%2CAD_GROUP_NAME%2CAD_GROUP_STATUS%2CCAMPAIGN_ID%2CCAMPAIGN_MANAGED_STATUS%2CCAMPAIGN_NAME%2CCAMPAIGN_STATUS%2CPIN_PROMOTION_NAME%2CPIN_PROMOTION_STATUS&granularity=DAY&level=PIN_PROMOTION&report_format=json&tag_version=3&view_window_days=60&metrics=ALL'.format(start_date, end_date)
        headers = {
            'Authorization': 'Bearer {}'.format(self.access_token),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        token = response.json()['data']['token']
        url = "https://api.pinterest.com/ads/v3/reports/async/{}/delivery_metrics/?token={}".format(ADVERTISER_ID, token)
        response = requests.request("GET", url, headers=headers)
        while response.json()['data']['report_status'] != 'FINISHED':
            response = requests.request("GET", url, headers=headers)
        report_url = response.json()['data']['url']
        return requests.get(report_url).json()
