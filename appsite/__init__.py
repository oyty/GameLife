# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_moment import Moment
from config import Config

# SQLAlchemy是一个强大的关系型数据库框架，mysql是数据库引擎
db = SQLAlchemy()
# 蓝本
bootstrap = Bootstrap()
# 日期处理的flask扩展
moment = Moment()
login_manager = LoginManager()
# 会话保护
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

# 让所有视图受CSRF保护
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    # config对象是一个字典，也可以从文件配置，头部导入Config文件
    app.config.from_object(Config)
    Config.init_app(app)

    # 以下为扩展的惰性加载
    csrf.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)


    # 注册蓝图
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
