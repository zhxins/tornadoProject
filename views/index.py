import tornado.web
from tornado.web import RequestHandler
import json
import os
import config
# from mysqlUtil import MySQLUtil
import MySQLdb as mdb
from tornado.httpclient import AsyncHTTPClient
from tornado.websocket import WebSocketHandler



# 视图
class IndexHandler(RequestHandler):
    def get(self):
        # self.write("hello ,tornado")
        self.write("<a href='/home'>jump another page</a>")

class HomeHandler(RequestHandler):

    # 接收参数
    def initialize(self, name, age):
        self.name = name
        self.age = age

    def get(self):
        print(self.name , self.age)
        # self.write("welcome to home index")
        title = "死亡如风，常伴吾身"
        def myMethod(s1, s2):
            return s1 + s2
        # 传递自定义函数
        self.render("home.html", title=title, method=myMethod)

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


class RedirectHandler(RequestHandler):

    def get(self):
        self.redirect("/login")


# 错误处理
class ErrorHandler (RequestHandler):

    def write_error(self, status_code: int, **kwargs):
        if status_code == 500:
            self.set_status(500)
            self.write("服务器内部错误")
        elif status_code == 404:
            self.set_status(404)
            self.write("资源不存在")

    def get(self):
        # 获取uir中指定参数的值，如果出现同名参数，则返回最后一个的值
        flag = self.get_query_argument("flag")
        print(type(flag))
        if flag == '0':
            # 需要和write_error配合使用
            self.send_error(500)
        self.write("request is ok")


class AdminHandler(RequestHandler):
    def get(self):
        # self.write("hello ,tornado")
        url = self.reverse_url("xadmin")
        print(url)
        self.write("<a href='%s'>jump another page</a>" %url)


'''uri传参'''
class LiuyifeiHandler(RequestHandler):

    # http://localhost:8080/liuyifei/nice/good/women
    # 打印结果为 nice-good-women，即取的是路由后后面的值
    def get(self, h1, h2, h3, *args, **kwargs):
        print(h1+"-"+h2+"-"+h3)
        self.write("liuyifeiHandler")


class ZhangmanyuHandler(RequestHandler):
    def get(self):
        # 获取uir中指定参数的值，如果出现同名参数，则返回最后一个的值
        # default 设置默认值，strip 去掉name两侧空格
        # self.get_query_arguments(name=a, default=10 strip=True)
        flag = self.get_query_argument("flag")
        self.write(flag);

        # 可接受两个name 为a 的值，返回值为列表
        alist = self.get_query_arguments("a")
        self.write(alist[0] + "--" + alist[1])


class PostFileHandler(RequestHandler):
    def get(self):
        self.render('postfile.html')

    def post(self):
        # post 请求接收参数
        username = self.get_body_argument("username")
        password = self.get_body_argument("password")
        hobbylist = self.get_body_arguments("hobby")

        print(username + '--' + password + '--' + hobbylist[1])
        self.write(username + '--' + password + '--' + hobbylist[0] + '--' + hobbylist[1] + '--' + hobbylist[2])


class ZhuyinHandler(RequestHandler):
    def get(self):
        print(self.request.method)
        print(self.request.host)
        print(self.request.uri)
        print(self.request.path)
        print(self.request.query)
        print(self.request.version)
        print(self.request.headers)
        print(self.request.body)
        print(self.request.remote_ip)
        print(self.request.files)
        self.write("zhuyinHandler request ok")


class UpfileHandler(RequestHandler):

    def initialize(self):
        print("initialize")

    def prepare(self):
        print("prepare")

    def set_default_headers(self):
        print("set_default_headers")

    def get(self):
        title = "hello,upfile"
        self.render('upfile.html', tt = title)

    def post(self):
        filesDict = self.request.files
        for inputname in filesDict:
            print('inputname:' + inputname)
            fileArr = filesDict[inputname]
            for fileObj in fileArr:
                filePath = os.path.join(config.BASE_DIRS, 'upload/' + fileObj.filename)
                with open(filePath, 'wb') as f:
                    f.write(fileObj.body)

                # 此处不知道为啥下面两种取值方式都可以
                print(fileObj['filename'])
                print(fileObj.filename)


        self.write("upload ok")


    def on_finish(self):
        print("on_finish method")


class TransHandler(RequestHandler):
    # tornado 默认开启了转义功能, 即下面字符串传到前台依然是字符串
    def get(self):
        str = "<h1>hello ,world</h1>"
        self.render("trans.html", str=str)

class ChildHandler(RequestHandler):
    def get(self):
        self.render("child.html", title="child page")


class StudentsHandler(RequestHandler):

    def get(self):
        # 从数据库中读取数据
        # tornado 没有自带的ORM，对于数据库需要自己去适配
        # 目前python3.6 + tornado还没有比较完善的驱动
        stus = self.application.db.get_all("select * from student")
        print(stus)

        # tup = (('1', 'jia', 11), ('2', 'rui', 25), ('3', 'fen', 39), ('4', 'koe', 45))
        # for item in tup:
        #     for t in item:
        #         print(t, end=' ')
        #     print()

        self.write("query ok")
        # self.render("students.html", stus = stus)


class CCookieHandler(RequestHandler):
    def get(self):
        # self.set_cookie(name, value, domain=None, expires=None, path="/", expires_days=1)
        # name: cookie名
        # value: cookie值
        # domain:提交cookie时匹配的域名
        # expires: cookie的有效期，可以是时间戳，时间元组，datatime类型
        # path: 提交cookie时匹配的路径
        # expires_day: cookie有效期天数，优先级小于expries
        self.set_cookie("hello", "world")
        self.write("cookie ok")


class getCCookieHandler(RequestHandler):
    def get(self):
        # 获取cookie，如果名为hello的cookie不存在，则返回default的值
        cookie = self.get_cookie("hello", default="未登录")

        # 清除cookie
        self.clear_cookie(name="", path="/", domain=None)
        print(cookie)

        # 清除所有cookie
        # self.clear_all_cookies()

        self.write("getCookie ok")


class getSCookieHandler(RequestHandler):
    def get(self):
        # 设置一个带有签名和时间戳的cookie,防止cookie被伪造
        # self.set_secure_cookie(name="", value="", expires_days=30, version=None, **kwargs)
        self.set_secure_cookie(name="secname", value="secret very good")

        # 获取安全cookie, 如果没取到name的值，则取value的值，max_age_days, 过滤安全cookie的时间戳，默认比设置的多一天
        # self.get_secure_cookie(name="", value="", max_age_days=31, min_version=None)
        # 也不是完全安全的，一定程度上增加了破解cookie的难度，
        # self.get_secure_cookie(name="", value="", max_age_days=31, min_version=None)
        self.get_secure_cookie(name="secname")


        self.write("secret cookie ok")


class CookieCountHandler(RequestHandler):
    def prepare(self):
        pass

    def get(self):
        count = self.get_cookie("count", None)
        if count:
            count = int(count)
            count += 1
        else:
            count = 1
        self.set_cookie("count", str(count))
        self.render("cookiecount.html", count=count)

    # 原来的get请求不安全，改为post即可
    # 表单提交，修改cookid
    def post(self):
        # 设置xsrf cookie
        self.xsrf_token
        pass


class LoginNewHandler(RequestHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        name = self.get_body_argument("username")
        pwd = self.get_body_argument("pwd")

        if name == "1" and pwd == "1":
            self.redirect("home.html?flag=logined")
            print("ads", name, pwd)
        else:
            self.redirect("login.html?flag=logined")


class HomeNewHandler(RequestHandler):
    def get_current_user(self):
        flag = self.get_arguments("flag", None)
        return flag

    @tornado.web.authenticated
    def get(self):
        self.render("homeNew.html")


# 回调异步
class LaoMianHandler(RequestHandler):
    def on_response(self, response):
        if response.error:
            self.send_error(500)
        else:
            # 转换成json串
            data = json.loads(response.body)
            self.write(data)
        self.finish()

    # @tornado.web.asynchronous    # 不关闭通信通道
    def get(self):
        # 创建客户端

        client = AsyncHTTPClient()
        url = "http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-"
        client.fetch(url, self.on_response)


# 协程异步
class YangrouHandler(RequestHandler):
    def on_response(self, response):
        if response.error:
            self.send_error(500)
        else:
            # 转换成json串
            data = json.loads(response.body)
            self.write(data)
        self.finish()


    @tornado.gen.coroutine
    def get(self):
        # 创建客户端

        client = AsyncHTTPClient()
        url = "http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-"
        res = yield client.fetch(url)
        if res.error:
            self.send_error(500)
        else:
            data = json.loads(res.body)
            self.write(data)


# 针对以上方法做出的优化改进操作
class KaojiHandler(RequestHandler):

    @tornado.gen.coroutine
    def get(self):
        res = yield self.getData()
        self.write(res)

    @tornado.gen.coroutine
    def getData(self):
        client = AsyncHTTPClient()
        url = "http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-"
        res = yield client.fetch(url)

        raise tornado.gen.Return(res)   # 把数据返回


class ChatInitHandler(RequestHandler):
    def get(self):
        self.render("chat1.html")


class ChatHandler(WebSocketHandler):

    # 存放连接人的信息
    users = []
    # 客户端建立连接后执行该方法
    def open(self):
        self.users.append(self)             # 添加用户信息
        # print(self.users)
        for user in self.users:
            # 主动向客户端发送message消息，可是字符串或字典
            # 如果binary(第二个参数)为False,则message会以UTF-8编码发送
            user.write_message(u"[%s]登录了" %(self.request.remote_ip))

    # 服务器主动关闭
    def close(self, code: int = None, reason: str = None):
        pass

    # 客户端发送消息调用
    def on_message(self, message):
        for user in self.users:
            # 主动向客户端发送message消息，可是字符串或字典
            # 如果binary(第二个参数)为False,则message会以UTF-8编码发送
            user.write_message(u"[%s]: %s" %(self.request.remote_ip, message))


    # 客户端主动关闭后调用
    def on_close(self):
        self.users.remove(self)
        for user in self.users:
            # 主动向客户端发送message消息，可是字符串或字典
            # 如果binary(第二个参数)为False,则message会以UTF-8编码发送
            user.write_message(u"[%s]下线了" % (self.request.remote_ip))


    # 判断是否同源，True为同源
    def check_origin(self, origin: str):
        return True



