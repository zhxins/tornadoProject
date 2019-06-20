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
            (r'/home', index.HomeHandler)

        ]

        super(Application, self).__init__(handlers)