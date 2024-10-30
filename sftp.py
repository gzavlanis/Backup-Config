import pysftp
from datetime import datetime
from helpers import createLog

class SFTPClient:
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.cnopts = pysftp.CnOpts()
        self.cnopts.hostkeys = None
        self.remote_path = None
        self.connection = None
        self.logger = createLog()

    def connect(self):
        try:
            self.connection = pysftp.Connection(
                host = self.hostname,
                username = self.username,
                password = self.password,
                cnopts = self.cnopts
            )
            self.logger.info('Connection successfully established.')
        except Exception as e:
            self.logger.error(f'Failed to connect: {e}')

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.logger.info('Connection closed.')

    def upload_file(self, local_path):
        if self.connection:
            date = datetime.now().strftime("%Y%m%d_%H%M")
            self.connection.put(local_path, f'./backup_{date}.sql')
            self.logger.info(f'File {local_path} uploaded successfully.')
