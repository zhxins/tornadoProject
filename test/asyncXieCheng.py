# 异步处理，两种实现方式回调和协程
# 协程处理

import time
import threading

gen = None

def longIO():
    def run():
        print("开始耗时操作")
        time.sleep(5)
        try:
            global gen
            gen.send("send data")
        except StopIteration as e:
            pass
        print("结束耗时操作")
    threading.Thread(target=run).start()


def finish(data):
    print("开始处理回调函数")
    print("回调结果：" + data)
    print("结束处理回调函数")


def reqA():
    print("开始处理A")
    res = yield longIO();
    print("res:" + res)
    print("结束处理A")


def reqB():
    print("开始处理B")
    print("结束处理B")


def main():
    global gen
    gen = reqA()   # 生成一个生成器
    next(gen)   # 执行reqA()
    reqB()
    while 1:
        time.sleep(1)

if __name__ == "__main__":
    main()