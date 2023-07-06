# -*- coding:utf-8 -*-
# @FileName  :woniuatm1.py
# @Time      :2023/7/6 10:14
# @Author    :dzz
# @Function  :
usename = ['zhangsan', 'lisi', 'wangwu']
password = ['1', '2', '3']


def reg():
    '''
    注册函数，如果注册失败或成功 退出系统
    :return:
    '''
    print("欢迎进入蜗牛ATM系统")
    name = input("请输入用户名(注册)")
    if name in usename:
        print("用户名已经存在")
        return False
    else:
        pw = input("请输入密码(注册)")
        if len(pw) < 6:
            print("密码长度小于6")
            return False
        print("注册成功 即将登陆系统")
        usename.append(name)
        password.append(pw)
        return True


def login():
    uname = input("请输入用户名")
    upass = input("请输入密码")
    if uname in usename:
        uindex = usename.index(uname)
        if password[uindex] == upass:
            print("恭喜你登陆成功")
        else:
            print("密码错误")
    else:
        print("用户名错误")
    pass


if __name__ == "__main__":
    if reg():
        login()
