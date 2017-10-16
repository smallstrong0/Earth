#! /usr/bin/env python
# -*- coding: utf8 -*-

import time
import datetime
import calendar


def get_ts():
    """
    :return: 获取当前时间轴
    """
    return long(time.time())


def get_ms():
    """
    :return: 获取当前时间轴 毫秒值
    """
    return long(time.time() * 1000)


def day2ts(day):
    """
    :param date: 2017-09-09
    :return: 时间轴
    """
    return time.mktime(time.strptime(day, '%Y-%m-%d'))


def day_cn2ts(day):
    """
    :param date: 2017年09月09日
    :return: 时间轴
    """
    return time.mktime(time.strptime(day, '%Y年%m月%d日'))


def time2ts(time):
    """
    :param time:  2017-09-09 11:11:11
    :return: 时间轴
    """
    return time.mktime(time.strptime(time, '%Y-%m-%d %H:%M:%S'))


def time_cn2ts(time):
    """
    :param time:  2017年09月09日 11:11:11
    :return: 时间轴
    """
    return time.mktime(time.strptime(time, '%Y年%m月%d日 %H:%M:%S'))


def get_month(ts=None):
    """
    :param ts: 时间轴
    :return: 获取时间轴月份
    """
    if ts is None:
        ts = get_ts()
    return time.strftime('%Y-%m', time.localtime(ts))


def get_month_cn(ts=None):
    if ts is None:
        ts = get_ts()
    return time.strftime('%Y年%m日', time.localtime(ts))


def get_day(ts=None):
    """
    :param ts: 时间轴
    :return: 返回时间轴对应的日子
    """
    if ts is None:
        ts = get_ts()
    return time.strftime('%Y-%m-%d', time.localtime(ts))


def get_day_cn(ts=None):
    """
    :param ts: 时间轴
    :return: 返回时间轴对应的日子 中文
    """
    if ts is None:
        ts = get_ts()
    return time.strftime('%Y年%m月%d日', time.localtime(ts))


def get_time(ts=None):
    """
    :param ts: 时间轴
    :return: 返回 %Y-%m-%d %H:%M:%S
    """
    if ts is None:
        ts = get_ts()
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))


def get_time_cn(ts=None):
    """
    :param ts: 时间轴
    :return: 返回 %Y年%m月%d日 %H:%M:%S
    """
    if ts is None:
        ts = get_ts()
    return time.strftime('%Y年%m月%d日 %H:%M:%S', time.localtime(ts))


def get_week_num():
    '''
    获取今天的星期
    :return: 0~6,0->Sunday
    '''
    l_time = time.localtime()
    return int(time.strftime('%w', l_time))


def get_today_zero_time(now=time.time()):
    """
    :param now: 时间轴
    :return: 传入时间轴当天的零点时间轴
    """
    midnight = now - (now % 86400) + time.timezone
    return long(midnight)


def get_last_month(date=None):
    """
    :param date: 时间轴
    :return: 当前时间轴 上月  ——> 2017-08
    """
    if not date:
        date = get_day()
    date_list = date.split('-')
    if int(date_list[1]) == 1:
        return '{}-12'.format(int(date_list[0]) - 1)

    return '{}-{}'.format(date_list[0], str(int(date_list[1]) - 1).zfill(2))


def get_week_first_day(ts=None):
    """
    :param ts: 时间轴
    :return: 当前时间轴本周的日期2017-09-04
    """
    if not ts:
        ts = get_ts()
    day = get_day(ts)
    time_list = day.split('-')
    week = calendar.weekday(int(time_list[0]), int(time_list[1]), int(time_list[2]))
    week_first_day = get_day(ts - week * 86400)
    return week_first_day


def get_week_first_timestamp(ts=None):
    """
    :param ts: 得到该时间轴 这周星期一起始时间轴
    :return:
    """
    a = '{} 00:00:01'.format(get_week_first_day(ts))
    s = time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S'))
    return long(s)


def d_value_day(ts, now_ts=get_ts()):
    """
    :param ts: 之前的时间轴
    :param now_ts: 现在的时间轴
    :return: 相差天数
    """
    d1 = get_day(ts)
    d2 = get_day(now_ts)
    date_list1 = d1.split('-')
    date_list2 = d2.split('-')
    d1 = datetime.datetime(int(date_list1[0]), int(date_list1[1]), int(date_list1[2]))
    d2 = datetime.datetime(int(date_list2[0]), int(date_list2[1]), int(date_list2[2]))
    return (d2 - d1).days


def get_weekenk_time(ctime, ts):
    '''
    :param ctime:
    :param ts:
    :return: 输出ctime所在周截止到ts 的周末时间
    '''
    saturday_start_stamp, sunday_end_time = get_weekenk_full_stamp(ctime)
    if ctime <= saturday_start_stamp:
        if ts <= sunday_end_time and ts > saturday_start_stamp:
            return ts - saturday_start_stamp
        elif ts <= saturday_start_stamp:
            return 0
        else:
            return 86400 * 2
    else:
        if ts <= sunday_end_time:
            return ts - ctime
        else:
            return sunday_end_time - ctime


def get_today_zero_time():
    return day2ts(get_day())


def get_weekenk_full_stamp(ctime):
    '''
    :param ctime: 传入 一个时间轴
    :return:   输出 这个时间轴对应的这个周的周末的 起始时间自 和结束时间轴
    '''
    str = time.strftime("%Y-%m-%d", time.localtime(ctime))
    c_start_stamp = long(time.mktime(time.strptime(str, '%Y-%m-%d')))

    day = time.localtime(ctime).tm_wday
    if day == 5:
        return c_start_stamp, c_start_stamp + 86400 * 2 - 1
    elif day == 6:
        return c_start_stamp - 86400, c_start_stamp + 86400 - 1
    else:
        saturday_start_stamp = (5 - day) * 86400 + c_start_stamp
        return saturday_start_stamp, saturday_start_stamp + 86400 * 2 - 1


if __name__ == '__main__':
    print get_ts()
    print get_ms()
    print get_day(get_ts())
    print get_day_cn(get_ts())
    print get_week_num()
    print get_today_zero_time()
    print get_last_month()
    print get_week_first_day()
    print get_weekenk_full_stamp(get_ts())
