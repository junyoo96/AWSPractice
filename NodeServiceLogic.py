import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from StoreLogic.NodeStoreLogic import  NodeStoreLogic

class NodeServiceLogic:

    def getAllNodes(self):

        nodeStoreLogic=NodeStoreLogic()

        return nodeStoreLogic.selectAllNodes()

    #자기만의 노드이름등록
    def nameNode(self):

        return '1'

    #노드추가
    def addNode(self):
        return '1'

    #노드수정
    def modifyNode(self):
        return '1'

    #노드삭제
    def removeNode(self):
        return '1'