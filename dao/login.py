import core.mongo as db_core
import tool.c_utils
import tool.t_utils

# login 表
collection = db_core.DbUtils().db.login


def create(dic={}):
    dic['ctime'] = tool.t_utils.get_ts()
    dic['mtime'] = tool.t_utils.get_ts()
    code = collection.insert(dic)
    if code:
        return dic
    else:
        return None


def update(old={}, new={}):
    return True if collection.update(old, {'$set': new}) else False


def select(where={}, field=[], limits=3, ordering=[]):
    return collection.find(where, field).limit(limits).sort(ordering)


def delete(field={}):
    return True if collection.remove(field) else False
