import requests
import urllib
tokenRequestURL = "https://api.brandwatch.com/oauth/token?username=" + BW_USERNAME +"&password="+ BW_PASSWORD +"&grant_type=api-password&client_id=brandwatch-api-client"

response = requests.get(tokenRequestURL).json()
Access_Token = response['access_token']
EncodedAccessToken = urllib.parse.quote(response['access_token'], safe='')
context.updateVariable("BW_ACCESS_TOKEN", EncodedAccessToken)
print(BW_ACCESS_TOKEN)


import requests
import math

cursor_list=''
rowCountRequest = "https://api.brandwatch.com/projects/" + BW_PROJECT_ID + "/data/mentions.json?queryId=" +BW_QUERY_ID + "&startDate="+ BW_DURATION_START_DATE +"&endDate=" +BW_END_DATE + "&pageSize=5000&page=0&access_token=" + BW_ACCESS_TOKEN
print(rowCountRequest)

response = requests.get(rowCountRequest).json()
batches = math.ceil(response['resultsTotal'] /5000)
context.updateVariable('BW_ITERATIONS',str(batches))

print(BW_ITERATIONS)

if BW_ITERATIONS!=1:
  cursor=''
  for i in range(int(BW_ITERATIONS)-1):
    request="https://api.brandwatch.com/projects/" + BW_PROJECT_ID + "/data/mentions.json?queryId=" +BW_QUERY_ID + "&startDate="+ BW_DURATION_START_DATE +"&endDate=" +BW_END_DATE + "&pageSize=5000&page=0&cursor="+cursor+"&access_token=" + BW_ACCESS_TOKEN
    response=requests.get(request).json()
    cursor=response['nextCursor']
    cursor_list=cursor_list+','+cursor
    
context.updateVariable('BW_CURSOR_LIST',cursor_list)

print('BW_CURSOR_LIST: '+BW_CURSOR_LIST)
  
  