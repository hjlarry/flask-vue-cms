from flask import request, json

from .bp import admin_bp
from flask_server.utils import success, fail, get_cpu, get_sysinfo, get_memory, get_disk, get_user
from flask_server.models import OperationLog
from flask_server.ext import db


@admin_bp.route('/sysinfo')
def sysinfo():
    """获取系统信息
    ---
    tags:
    - 系统
    security:
    - api_key: []
    responses:
      200:
        description: 获取成功
        schema:
          type: object
          properties:
            code:
                type: int
            data:
                type: array
                $ref: '#/definitions/Module'
            message:
                type: string
        examples:
          code: 0
          data: [{}, {}]
          message: 'success'
    """
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
    """获取操作日志
    ---
    tags:
    - 系统
    security:
    - api_key: []
    responses:
      200:
        description: 获取成功
        schema:
          type: object
          properties:
            code:
                type: int
            data:
                type: object
            message:
                type: string
        examples:
          code: 0
          data: {'items': [{},{},{}], 'total': 200}
          message: 'success'
    """
    current_page = request.args.get('page', 1)
    per_page = request.args.get('limit', 10)
    path = request.args.get('path', '')
    input = request.args.get('input', '')
    query_result = OperationLog.query.filter(OperationLog.path.like('%' + path + '%')).filter(
        OperationLog.input.like('%' + input + '%')).order_by(
        OperationLog.id.desc())
    date = request.args.get('date')
    if date:
        zero, twenti_four = date + ' 00:00:00', date + ' 23:59:59'
        query_result = query_result.filter(OperationLog._created_at.between(zero, twenti_four))
    pagination = query_result.paginate(page=int(current_page), per_page=int(per_page))
    result = [item.to_json() for item in pagination.items]
    res = {
        'data': {
            'items': result,
            'total': pagination.total
        }
    }
    return success(res)


@admin_bp.route('/operation_log/delete', methods=['DELETE'])
def delete_operation_log():
    """删除操作日志，可批量删除
    ---
    tags:
    - 系统
    security:
    - api_key: []
    responses:
      200:
        description: 删除成功
        schema:
          type: object
          properties:
            code:
                type: int
            message:
                type: string
        examples:
          code: 0
          message: 'success'
    """
    data = json.loads(request.data)
    try:
        for item in data:
            log = OperationLog.query.get_or_404(item['id'])
            db.session.delete(log)
        db.session.commit()
        return success()
    except Exception:
        return fail(400)
