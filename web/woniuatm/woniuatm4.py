# -*- coding:utf-8 -*-
# @FileName  :woniuatm1.py
# @Time      :2023/7/6 10:14
# @Author    :dzz
# @Function  :

# 使用一个字典保存用户信息
users = [
    {'name': 'zhang', 'pw': '100', 'balance': 3000},
    {'name': 'wang', 'pw': '101', 'balance': 3000},
    {'name': 'li', 'pw': '102', 'balance': 0}
]
ifLogin = False
currentUser = None

def reg():
    '''
    注册函数，如果注册失败或成功 退出系统
    :return:
    '''
    print("欢迎进入蜗牛ATM系统")

    while True:
        name = input("请输入用户名(注册)")
        for user in users:
            if name == user.get('name'):
                print("用户名已经存在,请重新输入")
                break  # 跳出本次循序
        else:  # for 正常结束时 执行
            pw = input("请输入密码(注册)")
            if len(pw) < 6:
                print("密码长度小于6,请重新输入")
            else:
                # return False
                print("注册成功 奖励3000元")
                users.append({'name': name, 'pw': pw, 'balance': 3000})
                break


def login():
    ireturn = False  # 为了退出外层循序，内层循环退出的时候 将外层循环的标记进行修改   然后再判断外层循环的标记决定是否退出外层循环
    while True:
        uname = input("请输入用户名")
        upass = input("请输入密码")
        for user in users:
            if user.get('name') == uname and user.get('pw') == upass:
                print("恭喜你登陆成功")
                ireturn = True
                global ifLogin
                ifLogin = True
                global currentUser
                currentUser = uname
                break
        else:
            print("密码或用户名错误，请重新输入")
            # uname = input("请输入用户名")
        if ireturn:
            break

# 查询余额前 先判断用户是否登陆，如果没有登陆 提示登陆  如果登陆则显示当前用户的余额
def query_balance():

    if ifLogin:
        for user in users:
            if user.get('name') == currentUser:
                print(f"欢迎{currentUser}登陆系统，您的约为{user.get('balance')}")
                break
    else:
        print("请先登陆系统")
        login()


def get_menu():
    menu = '''
        ***********欢迎进入ATM系统*********************
        ************请选择操作*************************
        ************1.注册 2.登陆 3.查询余额 4.退出 *****

    '''
    while True:
        print(menu)
        option = input("请输入操作选项")  # input输入的都是字符串
        if option == '1':
            reg()
        elif option == '2':
            login()
        elif option == '3':
            # 查余额的时候 需要先登陆才行
            query_balance()
        elif option == '4':
            print("感谢你的使用")
            break
        else:
            print("菜单输入错误 请重新输入")


if __name__ == "__main__":
    get_menu()
