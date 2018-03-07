from .bp import admin_bp
from utils import success, fail, get_cpu, get_sysinfo, get_memory, get_network, get_disk, get_user


@admin_bp.route('/sysinfo')
def sysinfo():
    res = {
        'data': {
            'cpu': get_cpu(),
            'sys': get_sysinfo(),
            'mem': get_memory(),
            'disk': get_disk(),
            'user': get_user()
        }
    }
    return success(res)