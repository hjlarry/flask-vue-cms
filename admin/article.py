from flask import request, json

from .bp import admin_bp
from models import Article, Module
from utils import success, fail


@admin_bp.route('/article')
def articles():
    """获取资讯列表
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
    current_page = request.args.get('page') or 1
    per_page = request.args.get('limit') or 10
    module = request.args.get('module')
    if module and not module == 'all':
        pagination = Article.query.filter_by(module_id=module).paginate(int(current_page), per_page=int(per_page))
    else:
        pagination = Article.query.paginate(int(current_page), per_page=int(per_page))
    articles = pagination.items
    total = pagination.total
    result = []
    for item in articles:
        item = item.to_json()
        result.append(item)

    res = {
        'data': {
            'items': result,
            'total': total
        }
    }
    return success(res)


@admin_bp.route('/module')
def module():
    """获取模块
    ---
    tags:
    - 资讯
    security:
    - api_key: []
    responses:
      200:
        description: 首页模块列表
        schema:
          $ref: '#/definitions/ApiResponse'
        examples:
          code: 0
          data: [{}, {}]
          message: 'success'
    """
    modules = Module.get(num='all', child_num=0)
    res = {
        'data': modules
    }
    return success(res)


@admin_bp.route('/article/<int:id>')
def get_article(id):
    """获取单个资讯
    ---
    tags:
    - 资讯
    security:
    - api_key: []
    responses:
      200:
        description: 首页模块列表
        schema:
          $ref: '#/definitions/ApiResponse'
        examples:
          code: 0
          data: [{}, {}]
          message: 'success'
    """
    article = Article.query.get_or_404(id)
    res = {
        'data': article.to_json(fields=['title', 'order', 'id', 'thumb_pic', 'content', 'module_name', 'module_id'])
    }
    return success(res)


@admin_bp.route('/article/create', methods=['POST'])
def create_article():
    """创建资讯
    ---
    tags:
    - 资讯
    security:
    - api_key: []
    responses:
      200:
        description: 首页模块列表
        schema:
          $ref: '#/definitions/ApiResponse'
        examples:
          code: 0
          data: [{}, {}]
          message: 'success'
    """
    data = json.loads(request.data)
    data['module_id'] = None if not isinstance(data['module_id'], int) else data['module_id']
    Article.create(**data)
    return success()


@admin_bp.route('/article/edit', methods=['POST'])
def edit_article():
    """编辑资讯
    ---
    tags:
    - 资讯
    security:
    - api_key: []
    responses:
      200:
        description: 首页模块列表
        schema:
          $ref: '#/definitions/ApiResponse'
        examples:
          code: 0
          data: [{}, {}]
          message: 'success'
    """
    data = json.loads(request.data)
    data['module_id'] = None if not isinstance(data['module_id'], int) else data['module_id']
    article = Article.query.get_or_404(data['id'])
    article.update(**data)
    return success()


@admin_bp.route('/article/delete', methods=['POST'])
def delete_article():
    """删除资讯
    ---
    tags:
    - 资讯
    security:
    - api_key: []
    responses:
      200:
        description: 删除成功
        examples:
          code: 0
          data: [{}, {}]
          message: 'success'
    """
    data = json.loads(request.data)
    article = Article.query.get_or_404(data['id'])
    if article:
        article.delete()
        return success()
    return fail(400)
