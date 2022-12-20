from flask import Blueprint, request, json, current_app

from flask_server.utils import success, ApiResult, fail
from flask_server.models import Article, Module, ExpressionOffical
from flask_server.ext import cache, freezer

api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/home')
def home() -> ApiResult:
    """获取首页
    ---
    tags:
    - 前台API
    responses:
      200:
        description: 首页模块列表
        schema:
          $ref: '#/definitions/Module'
        examples:
          code: 0
          data: [{}, {}]
          message: 'success'
    """
    res = cache.get('home_json')
    if not res:
        modules = Module.get_item(10)
        result = []
        for m in modules:
            if m.template_id == 'i_5':
                item = m.to_json()

            else:
                item = m.to_json(2)
            for c in item['child']:
                if c['thumb_pic']:
                    c['thumb_pic'] = 'http://' + c['thumb_pic']
            result.append(item)

        res = {
            'data': result
        }

        cache.setex('home_json', current_app.config['EXPIRE_TIME'], json.dumps(res))

    else:
        res = json.loads(res)
    return success(res)


@api_bp.route('/search/<string:word>')
def search(word: str) -> ApiResult:
    """ 搜索接口
    ---
    tags:
    - 前台API
    parameters:
      - $ref: '#/parameters/current_page'
      - $ref: '#/parameters/search_word'
    responses:
      200:
        description: 搜索结果
        schema:
          $ref: '#/definitions/Article'
        examples:
          code: 0
          data: [{}, {}]
          message: 'success'
          meta:
           current_page: 1
           total: 10
    """
    current_page = request.args.get('page') or 1
    pagination = Article.query.filter(Article.title.like('%' + word + '%')).paginate(page=int(current_page), per_page=5)
    articles = pagination.items
    total = pagination.total
    result = []
    for article in articles:
        item = article.to_json()
        result.append(item)

    res = {
        'data': result,
        'meta': {
            'current_page': int(current_page),
            'total': total
        }
    }
    return success(res)


@api_bp.route('/expression_offical', methods=['POST'])
def expression_offical_add() -> ApiResult:
    """ 添加体验官
    ---
    tags:
    - 前台API
    parameters:
    - in: body
      name: body
      required: true
      schema:
        $ref: '#/parameters/add_expression_offical'
    responses:
      200:
        description: 添加成功
        examples:
          code: 0
          message: 'success'
    """

    data = request.form
    try:
        ExpressionOffical.create(**dict(data))
    except Exception as e:
        current_app.logger.exception(e)
        return fail()
    return success()


@freezer.register_generator
def home():
    """
    generate a static json file
    :return:
    """
    yield '/api/home'