# 异步处理，两种实现方式回调和协程

import time
import threading

def longIO(callback):
    def run(cb):
        print("开始耗时操作")
        time.sleep(5)
        print("结束耗时操作")
        cb("callback")
    threading.Thread(target=run, args=(callback, )).start()


def finish(data):
    print("开始处理回调函数")
    print("回调结果：" + data)
    print("结束处理回调函数")

def reqA():
    print("开始处理A")
    longIO(finish);
    print("结束处理A")


def reqB():
    print("开始处理B")
    print("结束处理B")


def main():
    reqA()
    reqB()
    while 1:
        time.sleep(1)

if __name__ == "__main__":
    main()