# -*- coding: utf-8 -*-

from fabric.api import env, local, cd, run
from fabric.context_managers import prefix


def production():
    """ 设置 production 环境 """
    env.hosts = ["small@smallstrong.site"]
    env.key_filename = "/path/to/key_file"


# env.password = "123456"	# password 和 keyfile 两者只需要一个就可以


def staging():
    """ 设置 staging 环境 """
    env.hosts = ["staging@111.111.111.111:22"]
    env.password = "123456"  # 如果不写密码，会在 fab 执行时有交互提示输入密码


def update():
    """ 服务器上更新代码、依赖和迁移 """
    # cd 用于在服务器上执行 cd 命令，本地环境对应的 api 是 lcd (local cd)
    with cd("/path/to/usercenter"), prefix("workon usercenter"):
        run("git pull")  # run 用于服务器上执行命令
        run("pip install -r requirements.txt")
        run("python manage.py db migrate")
        run("supervisorctl restart usercenter")


def deploy():
    update()
