from datetime import date
from dateutil.relativedelta import relativedelta
from google.cloud import storage
today=date.today()
Last_week=date.today()-relativedelta(days=7)
Bucket_Name='iv_files'
Folder_Path_Sales='MINI_Loyalty/Sales_'+str(today)+'.csv'
Folder_Path_Owner_Sales='MINI_Loyalty/PreviousOwnerSales_'+str(today)+'.csv'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/var/bq.service.account.json"
client = storage.Client('iv-data-platform')
bucket = client.get_bucket(Bucket_Name)
blob1 = bucket.blob(Folder_Path_Sales)
blob1.upload_from_string(SALES_FILE)
blob1 = bucket.blob(Folder_Path_Owner_Sales)
blob1.upload_from_string(OWNER_FILE)
context.updateVariable("SALES_FILE_PATH", 'gs://'+Bucket_Name+'/'+Folder_Path_Sales)
context.updateVariable("OWNER_FILE_PATH", 'gs://'+Bucket_Name+'/'+Folder_Path_Owner_Sales)
print(SALES_FILE_PATH)
print(OWNER_FILE_PATH)
print(LOYALTY_END_DATE)
print(LOYALTY_START_DATE)