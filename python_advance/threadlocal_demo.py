import threading

local_data = threading.local()

local_data.name = "local"  # 给local_data 添加一个name属性


class mythread(threading.Thread):

    def run(self):
        print("赋值前-子线程：", threading.currentThread().name, local_data.__dict__)
        local_data.name = threading.current_thread().name
        print("赋值后-子线程：", threading.currentThread().name, local_data.__dict__)


if __name__ == '__main__':
    print("开始前主线程：", local_data.__dict__)

    t1 = mythread()
    t2 = mythread()
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    print("结束后主线程：", local_data.__dict__)
