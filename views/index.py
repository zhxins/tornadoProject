import tornado.web
from tornado.web import RequestHandler


# 视图
class IndexHandler(RequestHandler):
    def get(self):
        self.write("hello ,tornado")


class HomeHandler(RequestHandler):
    def get(self):
        self.write("welcome to home index")