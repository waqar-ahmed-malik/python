import pysftp
import io
import logging
import datetime


logging.getLogger().setLevel(logging.INFO)

class SFTP:
    def __init__(self, host: str, username: str, password: str) -> None:
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        self.conn = pysftp.Connection(host, username=username, password=password, cnopts=cnopts)

    def read_file_from_sftp(self, file_path: str) -> bytes:
        file_buffer = io.BytesIO()
        self.conn.getfo(file_path, file_buffer)
        file_buffer.seek(0)
        logging.info('Successfully Read File {} from SFTP.'.format(file_path))
        return file_buffer

    def list_files(self, sftp_directory) -> list:
        files = []
        for attr in self.conn.listdir_attr(sftp_directory):
            # file_modified_datetime = datetime.datetime.utcfromtimestamp(attr.st_mtime)
            source_file_path = '{}/{}'.format(sftp_directory, attr.filename)
            files.append(source_file_path)
        return files

    def write_data(self, data: str, file_path: str):
        with self.conn.open('{}'.format(file_path), "w") as f:
            f.write(data)
