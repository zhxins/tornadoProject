import tornado.web
from tornado.web import RequestHandler
import json
import config


# 视图
class IndexHandler(RequestHandler):
    def get(self):
        self.write("hello ,tornado")


class HomeHandler(RequestHandler):

    # 接收参数
    def initialize(self, name, age):
        self.name = name
        self.age = age

    def get(self):
        print(self.name , self.age)
        self.write("welcome to home index")


class LoginHandler(RequestHandler):

    def get(self):
        user = {
            "name" : "user",
            "age" : "12",
            "sex" : "男"
        }

        josnStr = json.dumps(user)
        self.set_header("Content-Type", "application/json;charset=UTF-8")
        self.write(josnStr)


class OrderHandler(RequestHandler):

    # 不想在每个方法里面设置字符编码，可以在每个Handler的 set_default_headers()方法中统一设置
    def set_default_headers(self):
        self.set_header("Content-Type", "text/html;charset=UTF-8")

    def get(self):
        self.write("order handler")

    def post(self):
        pass


# 往前端发送状态码
class StatusCodeHandler(RequestHandler):
    def get(self):
        # self.set_status(200)

        # set_status()这个方法可接一个参数也可以接收两个参数，如果第一个参数是正常状态码，则第二个参数可默认不写（默认为None）,
        # 正常状态码指是网络请求通用的即200，404，500等
        self.set_status(800, "code diredtion")
        self.write("status code handler")
