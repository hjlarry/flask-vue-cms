from flask import json
from werkzeug.wrappers import Response
import psutil
import time
import socket
import netifaces
import os
from collections import namedtuple


class ApiResult(object):
    def __init__(self, value, status=200):
        self.value = value
        self.status = status

    def to_response(self):
        return Response(json.dumps(self.value), status=self.status, mimetype='application/json')


class ApiException(Exception):
    def __init__(self, message, status=400):
        self.message = message
        self.status = status

    def to_result(self):
        value = {'message': self.message, 'code': 1}
        return ApiResult(value, self.status)


def success(res=None, status=200):
    res = res or {}
    dct = {
        'message': 'success',
        'code': 0
    }
    if isinstance(res, dict):
        dct.update(res)
    return ApiResult(dct, status)


def fail(status=400, code=1):
    dct = {
        'message': 'fail',
        'code': code
    }
    return ApiResult(dct, status)


def get_cpu():
    return psutil.cpu_times_percent(0)._asdict()


def get_sysinfo():
    sysinfo = {
        'boot_time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(psutil.boot_time())),
        'load_avg(1m ago)': round(os.getloadavg()[0], 2),
        'load_avg(5m ago)': round(os.getloadavg()[1], 2),
        'load_avg(15m ago)': round(os.getloadavg()[2], 2),
        'num_cpu': psutil.cpu_count()
    }
    return sysinfo


def get_memory():
    return psutil.virtual_memory()._asdict()


def get_network():
    result = list()
    for key, value in psutil.net_if_addrs().items():
        for v in value:
            item = v._asdict()
            item.update({'Interface': key})
            item['family'] = netifaces.address_families[item['family']]
            result.append(item)
    return result


def get_disk(all_partitions=False):
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

def get_user():
    result = list()
    for u in psutil.users():
        item = u._asdict()
        item['started'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item['started']))
        result.append(item)
    return result