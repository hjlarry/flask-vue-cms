import json
from werkzeug.exceptions import NotFound
from webtest import Upload

from .factories import UserFactory
from models import Admin, Article, OperationLog, Module


class TestFrontEnd:
    """Front api"""

    def test_home(self, testapp):
        """Homepage api"""
        module = Module(title='test_module', order=1)
        module.save()
        res = testapp.get('/api/home')
        assert res.status_code == 200
        assert res.content_type == 'application/json'
        assert res.content_length > 0
        assert res.json['code'] == 0
        assert len(res.json['data']) > 0

    def test_search(self, testapp, article):
        """Search api"""
        res = testapp.get('/api/search/test')
        assert res.status_code == 200
        assert res.json['code'] == 0
        assert len(res.json['data']) > 0


class TestUser:
    """All about user api tests."""

    def test_login(self, user, testapp):
        """Login successful."""
        res = testapp.post_json('/admin/login', {'username': 'test123', 'password': 'test123'})
        assert res.status_code == 200
        assert res.json['code'] == 0
        assert res.json['message'] == 'success'
        assert 'token' in res.json['data']

        res2 = testapp.post_json('/admin/login', {'username': 'test123', 'password': 'wrong'}, status='*')
        assert res2.status_code == 401

    def test_logout(self, user, testapp, get_token):
        res = testapp.request('/admin/logout', method='POST', headers=get_token)
        assert res.status_code == 200
        assert res.json['code'] == 50014

    def test_get_userlist(self, user, testapp, get_token):
        res = testapp.request('/admin/user', method='GET', headers=get_token, status='*')
        assert res
        assert res.status_code == 200
        assert 'items' in res.json['data']

    def test_get_userinfo(self, user, testapp, get_token):
        res = testapp.get('/admin/info', params=dict(token=get_token['Authorization']))
        assert res.status_code == 200
        assert 'name' in res.json['data']

    def test_get_one_user(self, user, testapp, get_token):
        res = testapp.request('/admin/user/1', method='GET', headers=get_token)
        assert res.status_code == 200
        assert 'id' in res.json['data']

    def test_create_user(self, user, testapp, get_token):
        res = testapp.request('/admin/user/create', method='POST', headers=get_token,
                              body=json.dumps(dict(username='testcreate', password='testcreate')).encode())
        assert res.status_code == 200
        assert res.json['code'] == 0

    def test_update_user(self, user, testapp, get_token):
        res = testapp.request('/admin/user/edit/1', method='PUT', headers=get_token,
                              body=json.dumps(dict(username='testcreate', password='testcreate')).encode())
        assert res.status_code == 200
        assert res.json['code'] == 0

        # test the username have not changed and the password has changed
        user = Admin.query.get_or_404(1)
        assert not user.username == 'testcreate'
        assert user.verify_password('testcreate')

    def test_delete_user(self, user, testapp, get_token):
        user = UserFactory(username='delete123', password='test123')
        user.save()
        res = testapp.request('/admin/user/delete/2', method='DELETE', headers=get_token)
        assert res.status_code == 200
        assert res.json['code'] == 0

        # test the user has removed
        try:
            user = Admin.query.get_or_404(2)
        except NotFound:
            user = None
        assert not user

    def test_upload_avatar(self, user, testapp, get_token):
        res = testapp.post('/admin/upload_avatar', dict(avatar=Upload('tests/test_avatar.png')),
                           headers=get_token)
        assert res.status_code == 200
        assert res.json['code'] == 0
        assert 'fileurl' in res.json['data']


class TestArticle:
    """All about aricle api tests."""

    def test_get_articlelist(self, article, testapp, get_token):
        res = testapp.request('/admin/article', method='GET', headers=get_token)
        assert res.status_code == 200
        assert 'items' in res.json['data']

    def test_get_modulelist(self, article, testapp, get_token):
        res = testapp.request('/admin/module', method='GET', headers=get_token)
        assert res.status_code == 200
        assert res.json['code'] == 0

    def test_get_one_article(self, article, testapp, get_token):
        res = testapp.request('/admin/article/1', method='GET', headers=get_token)
        assert res.status_code == 200
        assert 'id' in res.json['data']

    def test_create_article(self, article, testapp, get_token):
        res = testapp.request('/admin/article/create', method='POST', headers=get_token,
                              body=json.dumps(dict(title='testcreate', content='testcreate', module_id='')).encode())
        assert res
        assert res.status_code == 200
        assert res.json['code'] == 0

    def test_update_article(self, article, testapp, get_token):
        res = testapp.request('/admin/article/edit/1', method='PUT', headers=get_token, body=json.dumps(
            dict(title='testcreate22', content='testcreate22', module_id='')).encode())
        assert res.status_code == 200
        assert res.json['code'] == 0

        # test the article has changed
        article = Article.query.get_or_404(1)
        assert article.title == 'testcreate22'
        assert article.content == 'testcreate22'

    def test_delete_article(self, article, testapp, get_token):
        res = testapp.request('/admin/article/delete/1', method='DELETE', headers=get_token)
        assert res.status_code == 200
        assert res.json['code'] == 0


class TestSystem:
    """All about aricle api tests."""

    def test_get_sysinfo(self, user, testapp, get_token):
        res = testapp.request('/admin/sysinfo', method='GET', headers=get_token)
        assert res.status_code == 200
        assert 'cpu' in res.json['data']

    def test_get_operation_log_list(self, user, testapp, get_token):
        res = testapp.request('/admin/operation_log', method='GET', headers=get_token, status='*')
        assert res
        assert res.status_code == 200
        assert res.json['code'] == 0
        assert 'items' in res.json['data']

    def test_delete_operation_log(self, user, testapp, get_token):
        log1 = OperationLog(path='/test1')
        log2 = OperationLog(path='/test2')
        log1.save()
        log2.save()
        res = testapp.request('/admin/operation_log/delete', method='DELETE', headers=get_token, body=json.dumps(
            [dict(id=log1.id), dict(id=log2.id)]).encode())
        assert res.status_code == 200
        assert res.json['code'] == 0
