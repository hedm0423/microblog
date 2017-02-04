from app import app
from flask import request
@app.route('/')
@app.route('/index')
def index():
    return "Hello world"

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' %name

@app.route('/request')
def request():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' %user_agent

from flask import make_response
@app.route('/response')
def response():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer','42')
    return response
