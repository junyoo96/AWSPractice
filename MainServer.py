import os
import sys

from flask import Flask
from Controller.NodeController import NodeController_index

app=Flask(__name__)

app.register_blueprint(NodeController_index)

if __name__=='__main__':
	#app.run(host='0.0.0.0',port='5000',debug='True')
	app.run(debug='True')