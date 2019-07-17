#同步处理
import time


def longIO():
    print("开始耗时操作")
    time.sleep(5)
    print("开始耗时操作")


def reqA():
    print("开始处理A")
    longIO();
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