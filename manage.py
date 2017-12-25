#!/usr/bin/env python
# coding=utf-8
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from appsite import create_app, db
from appsite.models import ArticleType, article_types, Source, \
    Comment, Article, User, Menu, ArticleTypeSetting, BlogInfo, \
    Plugin, BlogView, Tag, Motto, tag_map


app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
# 在终端环境下添加一个db命令
manager.add_command('db', MigrateCommand)


# Global variables to jiajia2 environment:
app.jinja_env.globals['ArticleType'] = ArticleType
app.jinja_env.globals['article_types'] = article_types
app.jinja_env.globals['Menu'] = Menu
app.jinja_env.globals['BlogInfo'] = BlogInfo
app.jinja_env.globals['Plugin'] = Plugin
app.jinja_env.globals['Source'] = Source
app.jinja_env.globals['Article'] = Article
app.jinja_env.globals['Comment'] = Comment
app.jinja_env.globals['BlogView'] = BlogView
app.jinja_env.globals['Tag'] = Tag
app.jinja_env.globals['Motto'] = Motto


def make_shell_context():
    return dict(app=app, db=db, ArticleType=ArticleType, Source=Source,
                Comment=Comment, Article=Article, User=User, Menu=Menu,
                ArticleTypeSetting=ArticleTypeSetting, BlogInfo=BlogInfo,
                Plugin=Plugin, BlogView=BlogView, Tag=Tag, tag_map=tag_map)

manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def deploy(deploy_type):
    from flask_migrate import upgrade
    from appsite.models import BlogInfo, User, ArticleTypeSetting, Source, \
        ArticleType, Plugin, BlogView, Comment, Tag, tag_map, Article, Menu, \
        Follow, Motto

    # upgrade database to the latest version
    # upgrade()

    if deploy_type == 'product':
        # step_1:insert basic blog info
        BlogInfo.insert_blog_info()
        # step_2:insert admin account
        User.insert_admin(email='togamelife@gmail.com', username='togamelife', password='togamelife')
        # step_3:insert system default setting
        ArticleTypeSetting.insert_system_setting()
        # step_4:insert default article sources
        Source.insert_sources()
        # step_5:insert default articleType
        ArticleType.insert_system_articleType()
        # step_6:insert system plugin
        Plugin.insert_system_plugin()
        # step_7:insert blog view
        BlogView.insert_view()
        # step_8:insert mottos
        # Motto.insert_mottos()

    # You must run `python manage.py deploy product` before run `python manage.py deploy test_data`
    if deploy_type == 'test_data':
        # step_1:insert navs
        Menu.insert_menus()
        # step_2:insert articleTypes
        ArticleType.insert_articleTypes()
        # step_3:generate random articles
        Article.generate_fake(100)
        # step_4:generate random comments
        Comment.generate_fake(300)
        # step_5:generate random replies
        Comment.generate_fake_replies(100)
        # step_4:generate random comments
        Comment.generate_fake(300)

    if deploy_type == 'motto':
        Motto.insert_mottos()

if __name__ == '__main__':
    manager.run()
