# -*- coding:utf-8 -*-
# @FileName  :woniuatm1.py
# @Time      :2023/7/6 10:14
# @Author    :dzz
# @Function  :

# 使用一个二维列表保存用户名和密码
users = [
    ['zhangsan', '1'],
    ['lisi', '2'],
    ['wangwu', '3']
]


def reg():
    '''
    注册函数，如果注册失败或成功 退出系统
    :return:
    '''
    print("欢迎进入蜗牛ATM系统")

    while True:
        name = input("请输入用户名(注册)")
        for user in users:
            if name == user[0]:
                print("用户名已经存在,请重新输入")
                break  # 跳出本次循序
        else:  # for 正常结束时 执行
            pw = input("请输入密码(注册)")
            if len(pw) < 6:
                print("密码长度小于6,请重新输入")
            else:
                # return False
                print("注册成功 即将登陆系统")
                users.append([name, pw])
                break


def login():
    ireturn = False # 为了退出外层循序，内层循环退出的时候 将外层循环的标记进行修改   然后再判断外层循环的标记决定是否退出外层循环
    while True:
        uname = input("请输入用户名")
        upass = input("请输入密码")
        for user in users:
            if user[0] == uname and user[1] == upass:
                print("恭喜你登陆成功")
                ireturn = True
                break
        else:
            print("密码或用户名错误，请重新输入")
            # uname = input("请输入用户名")
        if ireturn:
            break


def get_menu():
    menu = '''
        ***********欢迎进入ATM系统***********
        ************请选择操作***************
        ************1.注册 2.登陆 3.退出*****
        
    '''
    while True:
        print(menu)
        option = input("请输入操作选项")  # input输入的都是字符串
        if option == '1':
            reg()
        elif option == '2':
            login()
        elif option == '3':
            print("感谢你的使用")
            break
        else:
            print("菜单输入错误 请重新输入")


if __name__ == "__main__":
    get_menu()
