from flask import Flask, request

APP_VERSION = 'v1'
APP_BASEPATH = '/api/' + APP_VERSION
APP_SERVICE = 'name: sub, version: ' + APP_VERSION
APP_PORT = '8082'

app = Flask(__name__)
@app.route('/')
def hello():
    return {'world': 'welcome all : '+APP_SERVICE}