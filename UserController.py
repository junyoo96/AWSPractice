import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import jsonify

from MainServer import app

#사용자등록
@app.route('/registerUser', methods=['POST'])
def registerUser():

    return '1'