from server import app
import pytest
import json

@pytest.fixture
def client(request):
	return app.test_client()

def get(client, path):
	rv = client.get(path)
	return json.loads(rv.data)

def post(client, path, data):
	rv = client.post(path, data=data, content_type='application/json')
	return json.loads(rv.data)

def test_search_items(client):
	item = {'title': 'to be searched', 'content': 'world'}
	add_res = post(client, '/add', json.dumps(item))

	search_res = get(client, '/search/searched')

	assert len(search_res['result']) > 0
	assert isinstance(search_res['result'][0]['item_id'], str)
	assert isinstance(search_res['result'][0]['title'], str)
	assert isinstance(search_res['result'][0]['content'], str)
	assert 'searched' in search_res['result'][0]['title'] or 'searched' in search_res['result'][0]['content']

def test_search_items_by_title(client):
	item = {'title': 'to be searched by title', 'content': 'world'}
	add_res = post(client, '/add', json.dumps(item))

	search_res = get(client, '/search_by_title/title')

	assert len(search_res['result']) > 0
	assert isinstance(search_res['result'][0]['item_id'], str)
	assert isinstance(search_res['result'][0]['title'], str)
	assert isinstance(search_res['result'][0]['content'], str)
	assert 'title' in search_res['result'][0]['title']

def test_search_items_by_content(client):
	item = {'title': 'hello', 'content': 'to be searched by content'}
	add_res = post(client, '/add', json.dumps(item))

	search_res = get(client, '/search_by_content/content')

	assert len(search_res['result']) > 0
	assert isinstance(search_res['result'][0]['item_id'], str)
	assert isinstance(search_res['result'][0]['title'], str)
	assert isinstance(search_res['result'][0]['content'], str)
	assert 'content' in search_res['result'][0]['content']
