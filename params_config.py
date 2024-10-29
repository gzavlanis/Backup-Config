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
        else:
            encrypted = toBytes(self.params)
            return decrypt(encrypted, self.key, self.iv)

    def getDBConfig(self):
        params = toJson(self.handleParamsFile())
        db = params['db']
        return db['host'], db['port'], db['user'], db['password'], db['database']