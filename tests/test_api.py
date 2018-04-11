from .factories import UserFactory


def get_token(testapp):
    user = UserFactory(username='admin123', password='admin123')
    user.save()
    res = testapp.post_json('/admin/login', {'username': 'admin123', 'password': 'admin123'})
    return dict(Authorization=res.json['data']['token'])


class TestFrontEnd:
    """Front API"""

    def test_home(self, user, testapp):
        """Homepage api"""
        res = testapp.get('/api/home')
        assert res.status_int == 200
        assert res.content_type == 'application/json'
        assert res.content_length > 0


class TestLogin:
    """Admin Login."""

    def test_log_in_can_return_200(self, user, testapp):
        """Login successful."""
        user = UserFactory(username='test123', password='test123')
        user.save()
        res = testapp.post_json('/admin/login', {'username': 'test123', 'password': 'test123'})
        assert res.status_code == 200
        assert res.json['code'] == 0
        assert res.json['message'] == 'success'
        assert 'token' in res.json['data']

        res2 = testapp.post_json('/admin/login', {'username': 'test123', 'password': 'wrong'}, status='*')
        assert res2.status_code == 401

    def test_logout_can_return_200(self, user, testapp):
        res = testapp.request('/admin/logout', method='POST', headers=get_token(testapp))
        assert res.status_code == 200
        assert res.json['code'] == 50014

    def test_get_user(self, user, testapp):
        res = testapp.request('/admin/user', method='GET', headers=get_token(testapp))
        assert res.status_code == 200
        assert 'items' in res.json['data']
