from params_config import Config
from backup_config import BackupConfig
from sftp import SFTPClient
from helpers import deleteLogs

def main():
    deleteLogs()
    config = Config()
    host, port, user, password, database = config.getDBConfig()
    sftpHost, sftpUser, sftpPassword = config.getSFTPConfig()

    backupConfig = BackupConfig(host, port, user, password, database)
    backupConfig.runCommand()

    sftpClient = SFTPClient(sftpHost, sftpUser, sftpPassword)
    sftpClient.connect()
    localPath = backupConfig.getUploadedFile()
    sftpClient.upload_file(localPath)

if __name__ == "__main__":
    main()
