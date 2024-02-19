from flask import Flask
from .apps import index,api
from .config import config

def setConfig(app):
    app.template_folder = config.Config.template_folder
    app.config["SQLALCHEMY_DATABASE_URI"]= config.Config.DB_URL
    app.static_folder = config.Config.static_folder

def registerBlueprint(app):
    app.register_blueprint(index.index)
    app.register_blueprint(api.api_bp)
def create_app():
    app = Flask(__name__)
    #加载配置
    setConfig(app)
    #注册蓝图
    registerBlueprint(app)
    return app

