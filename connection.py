import pymysql

class MySQLConnection:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                password = self.password,
                database = self.database
            )
            if self.connection:
                print('Connection to MySQL was successful')
        except OSError as e:
            print(f'Error: {e}')
            self.connection = None

    def createCursor(self):
        return self.connection.cursor()

    def close(self):
        if self.connection:
            self.connection.close()
            print('Connection closed.')
