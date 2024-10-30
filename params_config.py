from pathlib import Path
from helpers import readFile, writeFile, isDict, encrypt, decrypt, toBytes, toJson

class Config:
    def __init__(self):
        self.projectPath = Path.cwd()
        self.paramsFile = self.projectPath / 'params'
        self.params = readFile(self.paramsFile).encode()
        self.isDict = isDict(self.params)
        self.databaseConfig = {}
        self.key = b'365374714867484D4C416D5655665345'
        self.iv = b'4D33644D32393448'

    def handleParamsFile(self):
        if self.isDict:
            encrypted = encrypt(self.params, self.key, self.iv)
            writeFile(self.paramsFile, encrypted)
            return self.params
        else:
            encrypted = toBytes(self.params)
            self.params = decrypt(encrypted, self.key, self.iv)

    def getDBConfig(self):
        self.handleParamsFile()
        self.params = toJson(self.params)
        db = self.params['db']
        return db['host'], db['port'], db['user'], db['password'], db['database']

    def getSFTPConfig(self):
        sftp = self.params['sftp']
        return sftp['hostname'], sftp['username'], sftp['password']
