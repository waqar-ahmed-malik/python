import sql_server_api
import logging
import azure_blob_api

logging.getLogger().setLevel(logging.INFO)
sql_server_host = 'tcp:gwmokan-sql.public.11cbe6368b68.database.windows.net,3342'
sql_server_database = 'MokanHistory' 
sql_server_username = 'mokan' 
sql_server_password = 'G00dw1ll@dmin@2020'
storage_connection_string  = 'DefaultEndpointsProtocol=https;AccountName=mokanhistory;AccountKey=CWt/VnYY2h+MBoz6typ36r+SSDcvYq7/eKyM23h7w5W4nac/Vks3AP/uw2SUidVxplz/9gJDR9/WyvZHjGoYsA==;EndpointSuffix=core.windows.net'
storage_container_name = "mokanhistory"


sql_server_client = sql_server_api.SQLServer(sql_server_host, sql_server_database, sql_server_username, sql_server_password)
blob_storage_client = azure_blob_api.BLOBStorage(storage_connection_string)

logging.info('Connection Successful to SQL Server at {}@{}'.format(sql_server_username, sql_server_host))

avaialble_blobs = blob_storage_client.list_blobs(storage_container_name)
processed_tables = ['.'.join(blob_name.split('/')[-1].split('.')[:-1]) for blob_name in avaialble_blobs]

tables = sql_server_client.list_tables()
for index, table in enumerate(tables, start=1):
    if '{}.{}'.format(table["schema"], table["table"]) in processed_tables:
        logging.info('Transferred {} out of {} tables successfully.'.format(index, len(tables)))
        continue
    logging.info('Extracting {}.{} into CSV.'.format(table["schema"], table["table"]))
    sql_server_client.dump_to_csv('data.csv', table['schema'], table['table'])
    logging.info('Extracted table {}.{} into data.csv'.format(table["schema"], table["table"]))
    blob_storage_client.upload_blob(storage_container_name, 'data.csv', '{}.{}.csv'.format(table["schema"], table["table"]))
    logging.info('Extracted table {}.{} into {}.{}.csv and uploaded to {}'.format(table["schema"], table["table"], table["schema"], table["table"], storage_container_name))
    logging.info('Transferred {} out of {} tables successfully.'.format(index, len(tables)))
