import sys
import socket
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort


# 定义测试环境
dev = socket.gethostname() == 'yuanjie-Mac.local'
app = Flask(__name__)
api = Api(app)


##############################################################################
# App

class PushApp(Resource):
    def get(self):
        return {"hello": "world"}

api.add_resource(PushApp, '/ai')

app.run('0.0.0.0', 8000)
