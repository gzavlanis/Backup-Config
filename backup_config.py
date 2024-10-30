import subprocess, os
from datetime import datetime
from helpers import createLog

class BackupConfig:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.today = datetime.now().strftime("%Y%m%d_%H%M")
        self.directory = './backups'
        self.sqlFile = f'{self.directory}/backup_{self.today}.sql'
        self.command = f'mysqldump --no-tablespaces -h {self.host} -u {self.user} -p{self.password} {self.database} > {self.sqlFile}'
        self.logger = createLog()

    def runCommand(self):
        try:
            if not os.path.exists(self.directory):
                os.makedirs(self.directory)

            result = subprocess.run(self.command, shell = True)
            self.logger.info('Command output: %s', result.stdout)
            self.logger.info(f'Database backup saved to {self.sqlFile}')
        except subprocess.CalledProcessError as e:
            self.logger.error(f'Error: {e}')

    def getUploadedFile(self):
        if os.path.exists(self.sqlFile):
            return self.sqlFile
        else:
            self.logger.error('File not found!')