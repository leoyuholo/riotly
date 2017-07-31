from server import app
import pytest
import json

@pytest.fixture
def client(request):
	return app.test_client()

def post(client, path, data):
	rv = client.post(path, data=data, content_type='application/json')
	return json.loads(rv.data)

def test_add_item(client):
	item = {'title': 'hello', 'content': 'world'}
	res = post(client, '/add', json.dumps(item))

	assert isinstance(res['result']['item_id'], str)
	assert res['result']['title'] == 'hello'
	assert res['result']['content'] == 'world'

def test_remove_item(client):
	item = {'title': 'will be removed', 'content': 'hello world'}
	add_res = post(client, '/add', json.dumps(item))

	remove_res = post(client, '/remove', json.dumps({'item_id': add_res['result']['item_id']}))

	assert remove_res['result']

def test_star_item(client):
	item = {'title': 'will be starred', 'content': 'hello world'}
	add_res = post(client, '/add', json.dumps(item))

	star_res = post(client, '/star', json.dumps({'item_id': add_res['result']['item_id']}))

	assert star_res['result']['item_id'] == add_res['result']['item_id']
	assert star_res['result']['starred']

def test_unstar_item(client):
	item = {'title': 'will be unstarred', 'content': 'hello world'}
	add_res = post(client, '/add', json.dumps(item))

	star_res = post(client, '/star', json.dumps({'item_id': add_res['result']['item_id']}))

	assert star_res['result']['item_id'] == add_res['result']['item_id']
	assert star_res['result']['starred']

	unstar_res = post(client, '/unstar', json.dumps({'item_id': add_res['result']['item_id']}))

	assert unstar_res['result']['item_id'] == add_res['result']['item_id']
	assert unstar_res['result']['starred'] == False

def test_list_items(client):
	item = {'title': 'to be listed', 'content': 'hello world'}
	add_res = post(client, '/add', json.dumps(item))

	list_res = json.loads(client.get('/list').data)

	assert len(list_res['result']) > 0
	assert isinstance(list_res['result'][0]['item_id'], str)
	assert isinstance(list_res['result'][0]['title'], str)
	assert isinstance(list_res['result'][0]['content'], str)
