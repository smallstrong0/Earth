#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/12 17:59
# @Author  : SmallStrong
# @Des     : 
# @File    : test.py
# @Software: PyCharm


def go():
    dic = {
        111: '1',
        2222: '2',
        22223: '2',
        22224: '2',
        22225: '2',
        22226: '2',
    }
    # i = (1, 2, 3)
    #
    # l = [1,2,3,4]
    #
    # for index, key in enumerate(l):
    #     print(index)
    #     print(key)
    #     yield index
    #     # print(dic[key])

    # for k, v in dic.items():
    #     print(k)
    #     print(v)
    # mygenerator = (x * x for x in range(3))
    # print(mygenerator)
    # for i in mygenerator:
    #     print(i)

    mygenerator = createGenerator()
    print(mygenerator)
    for i in mygenerator:
        print(i)


def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i * i


if __name__ == '__main__':
    # go()
    a = [2, 3, 1, 0]
    map(lambda x: x > 1, a)
    print(a)
    import time
    time.sleep(10)

    b = 1
    if b is None:
        print(111)
    else:
        print(222)
