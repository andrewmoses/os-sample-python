from flask import Flask
from flaskext.mysql import MySQL
import os

application = Flask(__name__)
mysql = MySQL()
application.config['MYSQL_DATABASE_USER'] = os.environ['MYSQL_DATABASE_USER']
application.config['MYSQL_DATABASE_PASSWORD'] = os.environ['MYSQL_DATABASE_PASSWORD']
application.config['MYSQL_DATABASE_DB'] = os.environ['MYSQL_DATABASE_DB']
application.config['MYSQL_DATABASE_HOST'] = os.environ['MYSQL_DATABASE_HOST']
mysql.init_app(application)

@application.route("/")
def hello():
	conn = mysql.connect()
	cursor =conn.cursor()
	cursor.execute("SELECT * from Persons")
	data = cursor.fetchAll()
	for each in data:
		print(each)
	return "Hello Sas!!"

if __name__ == "__main__":
    application.run()
