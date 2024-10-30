### Dump a MySQL Database into an SFTP server

This app dumps a MySQL database into an SQL script and then uploads this file into an SMTP server.

#### In order to run the program install the packages first:
```
pip install requirements.txt
```

#### Create an enviromental file of this form and name it "params":
```
{
	"db": {
		"host": "your host",
		"port": 4-digit number,
		"user": "username",
		"password": "password",
		"database": "database name"
	},
	"sftp": {
        "hostname": "hostname",
        "username": "username",
        "password": "password"
	}
}
```
#### Create your own .exe file using PyInstaller:
```
pyinstaller --onefile --name your_executable_name --windowed main.py
```
After that, your executable will be inside the dist folder. You can move it wherever you want, but always along with the params file.
