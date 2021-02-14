import pyodbc


driver = '{ODBC Driver 17 for SQL Server}'

class SQLServer:
    def __init__(self, server: str, database: str, username: str, password: str, port: int=1433):
        self.conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password+';PORT='+str(port))
        self.database = database

    def __del__(self):
        self.conn.close()

    
    def list_tables(self):
        query = (
            """
            SELECT 
            schema_name(OBJECTS.schema_id), 
            OBJECTS.NAME,
            INDEXES.rowcnt 
            FROM sysindexes AS INDEXES
            INNER JOIN 
            sys.objects AS OBJECTS
            ON INDEXES.id = OBJECTS.object_id 
            WHERE INDEXES.indid < 2  AND OBJECTS.is_ms_shipped = 0 AND OBJECTS.type = 'U'
            """
        )
        cursor = self.conn.cursor()
        cursor.execute(query)
        tables = [{'schema': row[0], 'table': row[1], 'row_count': row[2]} for row in cursor.fetchall()]
        cursor.close()
        return tables


    def get_column_names(self, schema_name: str, table_name: str) -> list:
        cursor = self.conn.cursor()
        columns = cursor.columns(table=table_name, catalog=self.database, schema=schema_name).fetchall()
        columns = [column[3] for column in columns]
        cursor.close()
        return columns


    def dump_to_csv(self, csv_path: str, schema_name: str, table_name: str):
        query = 'SELECT * FROM {}.{}'.format(schema_name, table_name)
        cursor = self.conn.cursor()
        with open(csv_path, "w") as archi:
            columns = self.get_column_names(schema_name, table_name)
            archi.write(','.join(columns))
            archi.write('\n')
            print('Columns Written Successfully.')
            cursor.execute(query)
            i = 1
            for fila in cursor:
                registro = ''
                for campo in fila:
                    campo = str(campo)
                    registro = registro+str(campo)+";"
                registro = registro[:-1]
                registro = registro.replace('None','NULL')
                registro = registro.replace("'NULL'","NULL")
                archi.write(registro+"\n")
                print('Batch {} extracted successfully.'.format(i))
                i += 1