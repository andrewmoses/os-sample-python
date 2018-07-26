from flask import Flask, render_template
from flaskext.mysql import MySQL
import os
import json
from bson import json_util

application = Flask(__name__)
mysql = MySQL()
application.config['MYSQL_DATABASE_USER'] = os.environ['MYSQL_DATABASE_USER']
application.config['MYSQL_DATABASE_PASSWORD'] = os.environ['MYSQL_DATABASE_PASSWORD']
application.config['MYSQL_DATABASE_DB'] = os.environ['MYSQL_DATABASE_DB']
application.config['MYSQL_DATABASE_HOST'] = os.environ['MYSQL_DATABASE_HOST']
mysql.init_app(application)

@application.route("/")
def hello():
#	conn = mysql.connect()
#	cursor =conn.cursor()
#	cursor.execute("SELECT * from Persons")
#	data = cursor.fetchall()
#	for each in data:
#		print(each)
#	conn.close()
	return render_template('index.html')
# api end point to list all the records in posts
@application.route('/allposts', methods=['GET'])
def allposts():
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("SELECT * from posts")
	data = cursor.fetchall()
	row_headers=[x[0] for x in cursor.description] #this will extract row headers
	json_data=[]
	for result in data:
		json_data.append(dict(zip(row_headers,result)))
	conn.close()
	return json.dumps(json_data, default=json_util.default)

if __name__ == "__main__":
    application.run()
