import os
BASE_DIRS = os.path.dirname(__file__)

# 参数
options = {
    "port": 8080
}

mysql = {
    "host": "192.168.0.121",
    "user": "root",
    "pwd": "root",
    "dbName": "tornado"
}

settings = {
    #  告诉tornado从文件系统的某个特定位置提供静态文件
    "static_path": os.path.join(BASE_DIRS, "static"),
    "template_path": os.path.join(BASE_DIRS, "templates"),
    # "debug": True,
    "autoreload": False,
    # 关闭当前项目的自动转义，一般不建义使用
    # "autoescape": None
    # 配置安全cookie密钥
    "cookie_secret": "inQb079+S+G6DsyTZn2GbQIQ0/7zTEUrpt4uf8+MozA=",
    # 开启同源保护
    "xsrf_cookies": True,
    # 如果 authenticated验证失败，则跳转到下页面
    "login_url": "/home",
}

