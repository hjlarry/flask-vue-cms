from flask import json
from werkzeug.wrappers import Response
from collections import OrderedDict
import psutil
import time
import netifaces
import os
import shelve


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


class CacheDict():
    def __init__(self, db='cache.db'):
        self.db = db

    def get(self, key, default=None):
        key = str(key)
        with shelve.open(self.db) as db:
            if not key in db:
                return default
            elif db[key].get('expires', 0) < time.time():
                return default
            return db[key]['value']

    def set(self, key, value):
        key = str(key)
        with shelve.open(self.db) as db:
            db[key] = {
                'value': value
            }

    def expire(self, key, expire):
        key = str(key)
        with shelve.open(self.db, writeback=True) as db:
            db[key]['expires'] = time.time() + expire

    def delete(self, key):
        key = str(key)
        with shelve.open(self.db) as db:
            del db[key]

    def setex(self, key, time, value):
        self.set(key, value)
        self.expire(key, time)
