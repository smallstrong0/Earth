from pymongo import MongoClient


class DbUtils(object):
    def __init__(self):
        self.db = MongoClient(host='localhost', port=27017).power
