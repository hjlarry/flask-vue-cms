from flask import request, json


from .bp import admin_bp
from models import Article, Module
from utils import success, fail
from ext import db


@admin_bp.route('/article')
def articles():
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
    modules = Module.get(num='all', child_num=0)
    res = {
        'data': modules
    }
    return success(res)


@admin_bp.route('/article/<int:id>')
def get_article(id):
    article = Article.query.get_or_404(id)
    res = {
        'data': article.to_json(fields=['title', 'order', 'id', 'thumb_pic', 'content', 'module_name', 'module_id'])
    }
    return success(res)


@admin_bp.route('/article/create', methods=['POST'])
def create_article():
    data = json.loads(request.data)
    data['module_id'] = None if not isinstance(data['module_id'], int) else data['module_id']
    article = Article(title=data['title'], content=data['content'],
                      order=data['order'], module_id=data['module_id'], thumb_pic=data['thumb_pic'])
    db.session.add(article)
    db.session.commit()
    return success()


@admin_bp.route('/article/edit', methods=['POST'])
def edit_article():
    data = json.loads(request.data)
    data['module_id'] = None if not isinstance(data['module_id'], int) else data['module_id']
    article = Article.query.get_or_404(data['id'])
    article.title=data['title']
    article.content=data['content']
    article.order=data['order']
    article.module_id=data['module_id']
    article. thumb_pic=data['thumb_pic']
    db.session.add(article)
    db.session.commit()
    return success()


@admin_bp.route('/article/delete', methods=['POST'])
def delete_article():
    data = json.loads(request.data)
    article = Article.query.get_or_404(data['id'])
    if article:
        db.session.delete(article)
        db.session.commit()
        return success()
    return fail(400)