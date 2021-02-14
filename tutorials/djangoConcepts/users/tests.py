import pytds
import pandas
from google.cloud import bigquery


SQL_SERVER_HOST = '102.133.224.91'
SQL_SERVER_DATABASE = 'Company9'
SQL_SERVER_USERNAME = 'GoogleBigQuery'
SQL_SERVER_PASSWORD = '#query45big'
BQ_CONFIG_DATASET = 'CONFIG'
BQ_CONFIG_TABLE = 'SQL_SERVER_MIGRATION_CONFIG'
FUNCTION_ID = 1
MIGRATION_FREQUENCY = 'Hourly'
BQ_PROJECT_ID = 'sheets-to-syspro-connector'


client = bigquery.Client()
with pytds.connect(SQL_SERVER_HOST, SQL_SERVER_DATABASE, SQL_SERVER_USERNAME, SQL_SERVER_PASSWORD) as conn:
    query = "SELECT * FROM `{}.{}` WHERE Function_ID = {} AND Migration_Frequency = '{}'".format(BQ_CONFIG_DATASET,
                                                                                                 BQ_CONFIG_TABLE,
                                                                                                 FUNCTION_ID,
                                                                                                 MIGRATION_FREQUENCY)
    query_job = client.query(query)
    results = query_job.result()
    for row in results:
        i = 0
        try:
            query = "SELECT * FROM {}.{}".format(row['SQL_Server_Schema'], row['SQL_Server_Table'])
            for chunk in pandas.read_sql(sql=query, con=conn, coerce_float=True, chunksize=50000):
                chunk.columns = chunk.columns.str.replace('%', '_Percentage')
                if i == 0:
                    chunk.to_gbq(destination_table="{}.{}".format(row['BQ_Dataset'], row['BQ_Table']),
                                 project_id=BQ_PROJECT_ID, if_exists='replace')
                else:
                    chunk.to_gbq(destination_table="{}.{}".format(row['BQ_Dataset'], row['BQ_Table']),
                                 project_id=BQ_PROJECT_ID, if_exists='append')
                i += 1
                del chunk
            del i
        except Exception as e:
            print("Error in migrating {}".format(row['SQL_Server_Table']))
            print(e)
        else:
            continue