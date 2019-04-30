import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Database.DatabaseInstance import db

class UserStoreLogic:
    def registerUser(self):
        return '1'