import tornado.httpserver
import tornado.web
import config
from views import index
from application import Application

'''
手动创建服务器
tornado 的核心循环模块，封装了Linux的epoll和BSD的kqueue,是tornado高效的基础
'''

# tornado 默认启动的中一个进程，如何开启多个进程

if __name__ == "__main__":

    app = Application()
    # 手动实例化一个http服务器对象
    httpServer = tornado.httpserver.HTTPServer(app)
    # httpServer.listen(8000);

    # bind()，绑定端口
    httpServer.bind(config.options["port"])
    # httpServer.bind(9070)

    httpServer.start()

    # 每个子进程都会从父进程复制一份IOLoop的实例
    tornado.ioloop.IOLoop.current().start()
