from server import app
from flask_pymongo import PyMongo

mongo = PyMongo(app)

# mongo.db.item.create_index({'title': 'text', 'content': 'text'})
