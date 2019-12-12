import pysftp


File_Path='File_Name.csv'
SFTP_USERNAME = 'SFTP_USERNAME'
SFTP_PASSWORD = 'SFTP_PASSWORD'
SFTP_HOST = 'sftp.domain.com'


cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
with pysftp.Connection(SFTP_HOST, username=SFTP_USERNAME, password=SFTP_PASSWORD, cnopts = cnopts) as sftp:
    File_Flag=sftp.isfile(File_Path)
    Columns_Count = 0
    if File_Flag==True:
        with sftp.open(File_Path,mode='rb') as f:
            for line in f:
                print(line)
    else:
        print('No File Found')
