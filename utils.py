from flask import json
from werkzeug.wrappers import Response
from collections import OrderedDict, UserDict
import psutil
import time
import netifaces
import os


class ApiResult(object):
    def __init__(self, value: dict, status: int = 200):
        self.value = value
        self.status = status

    def to_response(self) -> Response:
        return Response(json.dumps(self.value), status=self.status, mimetype='application/json')


class ApiException(Exception):
    def __init__(self, message, status=400):
        self.message = message
        self.status = status

    def to_result(self):
        value = {'message': self.message, 'code': 1}
        return ApiResult(value, self.status)


def success(res: dict = None, status: int = 200) -> ApiResult:
    res = res or {}
    dct = {
        'message': 'success',
        'code': 0
    }
    if isinstance(res, dict):
        dct.update(res)
    # elif isinstance(res, bytes):
    #
    #     a = res.decode()
    #     b = json.loads(a)
    #     print(b)
    #     dct.update(b)
    return ApiResult(dct, status)


def fail(status: int = 400, code: int = 1) -> ApiResult:
    dct = {
        'message': 'fail',
        'code': code
    }
    return ApiResult(dct, status)


def get_cpu() -> OrderedDict:
    return psutil.cpu_times_percent(0)._asdict()


def get_sysinfo() -> dict:
    sysinfo = {
        'boot_time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(psutil.boot_time())),
        'load_avg(1m ago)': round(os.getloadavg()[0], 2),
        'load_avg(5m ago)': round(os.getloadavg()[1], 2),
        'load_avg(15m ago)': round(os.getloadavg()[2], 2),
        'num_cpu': psutil.cpu_count()
    }
    return sysinfo


def get_memory() -> OrderedDict:
    return psutil.virtual_memory()._asdict()


def get_network() -> list:
    result = list()
    for key, value in psutil.net_if_addrs().items():
        for v in value:
            item = v._asdict()
            item.update({'Interface': key})
            item['family'] = netifaces.address_families[item['family']]
            result.append(item)
    return result


def get_disk(all_partitions=False) -> list:
    disks = []
    for dp in psutil.disk_partitions(all_partitions):
        usage = psutil.disk_usage(dp.mountpoint)
        disk = {
            'device': dp.device,
            'mountpoint': dp.mountpoint,
            'type': dp.fstype,
            'options': dp.opts,
            'space_total': usage.total,
            'space_used': usage.used,
            'space_used_percent': usage.percent,
            'space_free': usage.free
        }
        disks.append(disk)

    return disks


def get_user() -> list:
    result = list()
    for u in psutil.users():
        item = u._asdict()
        item['started'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item['started']))
        result.append(item)
    return result


class CacheDict(UserDict):
    """尝试一个redis的替代方案，但尚未有好的办法存储全局变量，尤其用gunicorn以后需要是跨进程的通信"""
    def get(self, key, default=None):
        """如果设置了过期时间则先判断有没有过期，否则判断有没有设置过期时间"""
        if 't_' + key in self.data and self.data['t_' + key] < time.time():
            return self.data[key]
        elif key in self.data and 't_' + key not in self.data:
            return self.data[key]
        else:
            return default

    def set(self, key, value):
        self.data[key] = value

    def expire(self, key, expire):
        self.set('t_' + key, time.time() + expire)
