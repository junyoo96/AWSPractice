from flask import Flask
from flask import jsonify

#Oracle
import cx_Oracle

app=Flask(__name__)

@app.route('/')
def hello():
	return 'Welcome'

@app.route('/json')
def json_test():
	data={'hello' : 'world', 'number':3}
	resp=jsonify(data)	
	return resp

@app.route('/dbtest')
def db_test():
	con=cx_Oracle.connect('scott/12345678@oracle11gr2.cdubaygxhxxb.ap-northeast-2.rds.amazonaws.com:1521/orcl')
	print (con.version)
	con.close()	

if __name__=='__main__':
	app.run(host='0.0.0.0',port='5000')
