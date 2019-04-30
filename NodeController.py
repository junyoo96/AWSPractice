import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import jsonify
#from MainServer import app
from ServiceLogic.NodeServiceLogic import NodeServiceLogic

from flask import Blueprint

NodeController_index=Blueprint('NodeController_index',__name__)

#전체노드불러오기
# @app.route('/getAllNodes', methods=['POST'])
@NodeController_index.route('/getAllNodes')
def getAllNodes():

    nodeServiceLogic=NodeServiceLogic()
    NodeList=nodeServiceLogic.getAllNodes()

    datas = []
    data = {}
    for node in NodeList:
        print(node)
        data = {'node_id': node.node_id, 'node_type': node.node_type, 'node_name': node.node_name, 'pos_x': node.pos_x,
                'pos_y': node.pos_y, 'node_neighbors': node.neighbors}
        datas.append(data)
        data = {}

    sendData = {"Node": datas}

    resp = jsonify(sendData)

    return resp


#자기만의 노드이름등록
# @app.route('/nameNode', methods=['POST'])
# def nameNode():
#
#     return '1'
#
# #노드추가
# @app.route('/addNode', methods=['POST'])
# def addNode():
#     return '1'
#
# #노드수정
# @app.route('/modifyNode', methods=['POST'])
# def modifyNode():
#     return '1'
#
# #노드삭제
# @app.route('/removeNode', methods=['POST'])
# def removeNode():
#     return '1'


