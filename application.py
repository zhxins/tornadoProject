import tornado.web
from views import index
import config

'''
    路由配置
'''
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', index.IndexHandler),
            (r'/home', index.HomeHandler, {"name": "liming", "age": "11"}),
            (r'/login', index.LoginHandler),
            # 状态码
            (r'/status', index.StatusCodeHandler),
            # 重定向
            (r'/redir', index.RedirectHandler),
            # 错误处理
            # iserror?flag=2
            (r'/iserror', index.ErrorHandler),

            # 有name属性的话不能使用元组路由，必须使用以下路由
            # 反向解析
            tornado.web.url(r'/admin', index.AdminHandler, name="xadmin"),

            # 获取特定uri的参数
            (r'/liuyifei/(\w+)/(\w+)/(\w+)', index.LiuyifeiHandler),

            (r'/zhangmanyu', index.ZhangmanyuHandler),

            # post请求
            (r'/postfile', index.PostFileHandler),

            # request 请求
            (r'/zhuyin', index.ZhuyinHandler),

            # 上传文件
            (r'/upfile', index.UpfileHandler),

            # 转义
            (r'/trans', index.TransHandler),

            (r'/child', index.ChildHandler),


        ]

        # 加载配置文件
        super(Application, self).__init__(handlers, **config.settings)
        # super(Application, self).__init__(handlers)