from server import app
from server.mongo import mongo
from flask import jsonify
import re

@app.route('/search/<text>', methods=['GET'])
def search_items(text):
	# items = mongo.db.items.find({'$text': {'$search': text}})
	text_re = re.compile(text, re.IGNORECASE)
	items = mongo.db.items.find(
		{'$or': [
			{'title': text_re},
			{'content': text_re}
		]}
	)

	output = [{'item_id': str(item['_id']),
		'title': item['title'],
		'content': item['content'],
		'starred': item['starred']} for item in items]

	return jsonify({'result': output})

@app.route('/search_by_title/<title>', methods=['GET'])
def search_items_by_title(title):
	items = mongo.db.items.find({
		# '$text': {'$search': title},
		'title': re.compile(title, re.IGNORECASE)
	})

	output = [{'item_id': str(item['_id']),
		'title': item['title'],
		'content': item['content'],
		'starred': item['starred']} for item in items]

	return jsonify({'result': output})

@app.route('/search_by_content/<content>', methods=['GET'])
def search_items_by_content(content):
	items = mongo.db.items.find({
		# '$text': {'$search': content},
		'content': re.compile(content, re.IGNORECASE)
	})

	output = [{'item_id': str(item['_id']),
		'title': item['title'],
		'content': item['content'],
		'starred': item['starred']} for item in items]

	return jsonify({'result': output})
