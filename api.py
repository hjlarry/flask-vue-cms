from utils import success
from models import Article, Module
from redis_db import cache
from config import EXPIRE_TIME

from flask import Blueprint, request


api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/home')
def home():
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

        cache.set('home_json', res)
        cache.expire('home_json', EXPIRE_TIME)
    return success(res)


@api_bp.route('/search/<word>')
def search(word):
    current_page = request.args.get('page') or 1
    pagination = Article.query.filter(Article.title.like('%'+word+'%')).paginate(int(current_page), per_page=5)
    articles = pagination.items
    total = pagination.total
    result = []
    for article in articles:
        item = article.to_json()
        result.append(item)

    res = {
        'data': result,
        'meta': {
            'current_page' : current_page,
            'total': total
        }
    }
    return success(res)

