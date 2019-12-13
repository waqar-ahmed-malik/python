import pysftp


def get_file_data(file_path: str, username: str, password: str, host: str) -> list:
    data = []
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(SFTP_HOST, username=username, password=password, cnopts = cnopts) as sftp:
        File_Flag=sftp.isfile(file_path)
        if File_Flag==True:
            with sftp.open(file_path,mode='rb') as f:
                for line in f:
                    data.append(line)
    return data

