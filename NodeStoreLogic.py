import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Database.DatabaseInstance import db
from Domain.Node import Node

class NodeStoreLogic:

    def selectAllNodes(self):

        db.execute('SELECT * FROM NODE')
        records = db.fetchall()

        node_list=[]

        for record in records:

            print(record)

            #인접노드에 대한 것 리스트로 뽑아오기

            #리스트 뽑은거 리스트 형태로 Node생성자에 추가
            node=Node(record[0],record[2],record[3],record[4],record[1])
            node_list.append(node)

        return node_list


    #자기만의 노드이름등록
    def registerNodeName(self):

        return '1'

    #노드추가
    def insertNode(self):
        return '1'

    #노드수정
    def updateNode(self):
        return '1'

    #노드삭제
    def deleteNode(self):
        return '1'