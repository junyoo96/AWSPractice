import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import jsonify

from MainServer import app

#경로탐색
@app.route('/searchPath', methods=['POST'])
def searchPath():

    return '1'