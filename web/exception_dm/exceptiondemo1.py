# try:
#     a = eval(input("输入被除数"))
#     b = eval(input("输入除数"))
#     c = a / b
#     print("输入的两个数相除的结果为%f" % c)
#
# except(ArithmeticError) as e:
#     print(e)
# # except:  # 匹配所有的异常
# #     print("程序遇到了未知的错误")
#
# else:
#     print("程序未发生任何异常时执行的代码")
# finally:
#     print("不管是否发生异常，finally都会被执行 一般用户资源回收")
#
# # print(1/0) 异常捕获后 代码将正常执行完，如果没有捕获异常，程序将异常退出，后面的代码不再执行
# print("程序运行结束")
#
#
# def main():
#     a = eval(input("请输入a的值"))
#     try:
#         mtd(a)
#     except Exception as e:
#         # raise
#         print("异常喽",e)
#     print("程序运行完成")
#
#
# def mtd(a):
#     if a > 0:
#         raise
#
# if __name__ == '__main__':
#     main()

# 自定义异常
class AuctionException(Exception):
    pass


class Auciton:
    def __init__(self):
        self.price = 100

    def auction(self, price):
        if self.price > price:
            raise AuctionException("当前竞拍价不能小于起拍价")
        else:
            self.price = price


if __name__ == '__main__':
    au = Auciton()
    try:
        au.auction(1000)
        print(f"当前竞拍价格为{au.price}")
    except AuctionException as e:
        print(e)
