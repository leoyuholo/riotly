from flask import Flask, current_app

app = Flask('riotly')

app.config['MONGO_URI'] = 'mongodb://mongo:27017/riotly'

@app.route('/')
def root():
	return current_app.send_static_file('index.html')

from server.controllers import *
