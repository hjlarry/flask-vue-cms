from flask import request, json

from .bp import admin_bp
from utils import success, fail, get_cpu, get_sysinfo, get_memory, get_disk, get_user
from models import OperationLog
from ext import db


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


@admin_bp.route('/operation_log')
def operation_logs():
    current_page = request.args.get('page') or 1
    per_page = request.args.get('limit') or 10
    path = request.args.get('path')
    input = request.args.get('input')
    date = request.args.get('date')
    zero = date + ' 00:00:00'
    twenti_four = date + ' 23:59:59'
    pagination = OperationLog.query.filter(OperationLog.path.like('%' + path + '%')).filter(
        OperationLog.input.like('%' + input + '%')).filter(
        OperationLog._created_at.between(zero, twenti_four)).order_by(
        OperationLog.id.desc()).paginate(int(current_page), per_page=int(per_page))
    users = pagination.items
    total = pagination.total
    result = []
    for item in users:
        item = item.to_json()
        result.append(item)

    res = {
        'data': {
            'items': result,
            'total': total
        }
    }
    return success(res)


@admin_bp.route('/operation_log/delete', methods=['POST'])
def delete_operation_log():
    data = json.loads(request.data)
    try:
        for item in data:
            log = OperationLog.query.get_or_404(item['id'])
            db.session.delete(log)
        db.session.commit()
        return success()
    except Exception:
        return fail(400)
