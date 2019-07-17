应用安全包括Cookie、XSRF、用户验证
1、Cookie: 普通Cookie(set, get, clear), 安全Cookie
2、XSRF：同源策略
3、用户验证：

tornado 是单线程的，如果上一个请求阻塞（sleep(20)）,则下一人请求等待上一个请求完成再执行本次请求
tornado.httpclient.AsyncHTTPClient:tornado提供的异步web请求客户端，用来进行异步web请求
fetch(request.callback = None):用于执行一个web请求，并异步响应一个tornado.httpclient.HttpResponse,
    request可以是一个url，也可以是一个tornado.httpclient.HttpRequest
HTTPRequest, HTTP请求类，该类的构造函数可以接收参数
    url:字符串类型，要访问的网址，必传
    method: 字符串类型，请求方式
    headers: 字典类型或HTTPHeaders，附加协议头
    body; HTTP请求体
HTTPResponse, HTTP响应类，
    code：状态码
    reason:状态码的描述
    body: 响应数据
    err: 异常

实现异步的两种方式：回调函数和协程

