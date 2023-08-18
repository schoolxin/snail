# -*- coding:utf-8 -*-
# @FileName  :woniuatm1.py
# @Time      :2023/7/6 10:14
# @Author    :dzz
# @Function  : 增加存款 取款  转账的功能

# 使用一个字典保存用户信息
users = [
    {'name': 'zhang', 'pw': '100', 'balance': 3000},
    {'name': 'wang', 'pw': '101', 'balance': 3000},
    {'name': 'li', 'pw': '102', 'balance': 0}
]

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

                global currentUser
                currentUser = user
                break
        else:
            print("密码或用户名错误，请重新输入")
            # uname = input("请输入用户名")
        if ireturn:
            break


# 查询余额前 先判断用户是否登陆，如果没有登陆 提示登陆  如果登陆则显示当前用户的余额
def query_balance():
    if currentUser:
        print(f"欢迎{currentUser.get('name')}登陆系统，您的约为{currentUser.get('balance')}")
    else:
        print("请先登陆系统")
        login()


def deposit():
    # step 1 判断用户是否登陆
    if currentUser:
        money = input("欢迎存款,请输入存款金额")
        if money.isdigit() and money[-2:] == '00':
            currentUser['balance'] += int(money)
            print(f"恭喜你存款成功,当前余额为{currentUser['balance']}")

        else:
            print("存款的金额有问题请重新存款")
    else:
        print("用户未登陆，请先登陆")
        login()
    # step 2 判断输入的金额是否符合要求(100倍数的整数)


def withdraw():
    pass


def transfer():
    print("转账2222222222")


def get_menu():
    # transfer()
    menu = '''
        **********************欢迎进入ATM系统*************************************
        ************************请选择操作****************************************
        ********************1.注册 2.登陆 3.查询余额 4.存款 5.取款 6.转账 7.退出 *****

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
            deposit()  # 存款  存款的时候必须是100的整数倍 还要判断用户是否登陆
        elif option == '5':
            withdraw()  # 取款
        elif option == '6':
            transfer()  # 转账
        elif option == '7':
            print("感谢你的使用")
            break
        else:
            print("菜单输入错误 请重新输入")


if __name__ == "__main__":
    get_menu()
