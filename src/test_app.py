import pytest
from src.app import app


@pytest.fixture
def client():
    """建立測試客戶端"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_returns_html(client):
    """測試首頁是否回傳 HTML"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Flask' in response.data
    assert b'html' in response.data


def test_404_error(client):
    """測試 404 錯誤處理"""
    response = client.get('/nonexistent')
    assert response.status_code == 404
    assert b'404' in response.data
