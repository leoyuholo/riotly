from server import app
from server.mongo import mongo
from flask import jsonify
from flask import request
from flask_pymongo import ObjectId
from pymongo.collection import ReturnDocument

@app.route('/list', methods=['GET'])
def list_items():
	offset = request.args.get('offset')
	limit = request.args.get('limit')

	offset = 0 if not offset else int(offset)
	limit = 10 if not limit else int(limit)

	items = mongo.db.items.find(skip=offset, limit=limit)

	output = [{
		'item_id': str(item['_id']),
		'title': item['title'],
		'content': item['content'],
		'starred': item['starred']
	} for item in items]

	return jsonify({'result': output})

@app.route('/add', methods=['POST'])
def add_item():
	title = request.json['title']
	content = request.json['content']

	item_id = mongo.db.items.insert({
		'title': title,
		'content': content,
		'starred': False
	})

	new_item = mongo.db.items.find_one({'_id': item_id})

	output = {
		'item_id': str(new_item['_id']),
		'title': new_item['title'],
		'content': new_item['content'],
		'starred': new_item['starred']
	}

	return jsonify({'result': output})

@app.route('/remove', methods=['POST'])
def remove_item():
	item_id = request.json['item_id']

	mongo.db.items.find_one_and_delete({'_id': ObjectId(item_id)})

	return jsonify({'result': True})

@app.route('/star', methods=['POST'])
def star_item():
	item_id = request.json['item_id']

	item = mongo.db.items.find_one_and_update(
		{'_id': ObjectId(item_id)},
		{'$set': {'starred': True}},
		return_document=ReturnDocument.AFTER
	)

	output = {
		'item_id': str(item['_id']),
		'title': item['title'],
		'content': item['content'],
		'starred': item['starred']
	}

	return jsonify({'result': output})

@app.route('/unstar', methods=['POST'])
def unstar_item():
	item_id = request.json['item_id']

	item = mongo.db.items.find_one_and_update(
		{'_id': ObjectId(item_id)},
		{'$set': {'starred': False}},
		return_document=ReturnDocument.AFTER
	)

	output = {
		'item_id': str(item['_id']),
		'title': item['title'],
		'content': item['content'],
		'starred': item['starred']
	}

	return jsonify({'result': output})
