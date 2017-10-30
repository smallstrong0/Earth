import pymongo


class DbUtils(object):
    def __init__(self, db_name='power', collection_name=''):
        exec ("self.db = pymongo.MongoClient(host='localhost', port=27017)." + db_name)
        exec ("self.collection = self.db." + collection_name)

    def add(self, data=[]):
        return True if self.collection.insert_many(data) else False

    def update(self, old={}, new={}):
        return True if self.collection.update(old, {'$set': new}) else False

    def select(self, where={}, field=[], limits=3, ordering=[]):
        return self.collection.find(where, field).limit(limits).sort(ordering)

    def delete(self, field={}):
        return True if self.collection.remove(field) else False
