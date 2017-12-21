# coding=utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # 是否debug模式
    DEBUG = True

    def __init__(self):
        pass

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 每次请求结束后自动提交数据库中的变动
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

    print(SQLALCHEMY_DATABASE_URI)

    ARTICLES_PER_PAGE = 10
    COMMENTS_PER_PAGE = 6

    SECRET_KEY = 'secret key to protect from csrf'
    WTF_CSRF_SECRET_KEY = 'random key for form' # for csrf protection
    # Take good care of 'SECRET_KEY' and 'WTF_CSRF_SECRET_KEY', if you use the
    # bootstrap extension to create a form, it is Ok to use 'SECRET_KEY',
    # but when you use tha style like '{{ form.name.labey }}:{{ form.name() }}',
    # you must do this for yourself to use the wtf, more about this, you can
    # take a reference to the book <<Flask Framework Cookbook>>.
    # But the book only have the version of English.

    @staticmethod
    def init_app(app):
        pass
