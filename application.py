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
            (r'/home', index.HomeHandler, {"name": "liming","age":"11"}),
            (r'/login', index.LoginHandler),
            # 状态码
            (r'/status', index.StatusCodeHandler)
        ]

        super(Application, self).__init__(handlers, **config.settings)