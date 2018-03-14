from flask import Blueprint, request
from werkzeug.utils import secure_filename
import re
import time
import os

from config import UPLOAD_FOLDER
from utils import success, fail
from models import OperationLog
from ext import db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

CH_REGEX = re.compile(r'[\u4e00-\u9fff]+')
ALLOWED_EXTENSIONS = frozenset(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
ALLOWED_PATHS = frozenset(['/admin/login', '/admin/info'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@admin_bp.route('/upload', methods=['POST'])
def upload():
    """上传文件
    ---
    tags:
    - 资讯
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
    file = request.files['file']
    if file:
        now = time.time()
        date = time.strftime('%Y%m%d', time.localtime(now))
        filename = str(int(now)) + file.filename
        if not allowed_file(filename):
            return fail(415)
        if not CH_REGEX.search(filename):
            filename = secure_filename(filename)
        UPLOAD_PATH = os.path.join(UPLOAD_FOLDER, date)
        os.makedirs(UPLOAD_PATH, exist_ok=True)
        filepath = os.path.join(UPLOAD_PATH, filename)
        file.save(filepath)

        res = {'data':
            {
                'filename': filename,
                'fileurl': filepath
            }
        }
        return success(res)
    return fail(400)


@admin_bp.after_request
def verify_user(response):
    """
    对这个蓝图下的请求进行权限验证，同时增加操作日志
    :param response:  Flask Response Object
    :return: response
    """
    from .user import verify_token
    if request.path in ALLOWED_PATHS or request.method == 'OPTIONS':
        return response
    elif 'Authorization' in request.headers:
        data = verify_token(request.headers['Authorization'])
        if data:
            add_operation_log(data, request)
            return response
    return fail(200, 50014).to_response()


def add_operation_log(data, request):
    log = OperationLog(user_id=data['user_id'], path=request.full_path,
                       ip=request.remote_addr, method=request.method, input=request.get_json())
    db.session.add(log)
    db.session.commit()
