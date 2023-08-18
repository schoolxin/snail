from woniuatm_class.menu import Menu
from woniuatm_class.user import User


class Bank:
    def __init__(self):
        self.meun = Menu()
        self.user_list = [
            User('zhang', '1001', 2000),
            User('lisi', '1002', 2000),
            User('wang', '1003', 3000)
        ]  # 初始化用户列表
        self.current_user = None

    def option(self):
        while True:
            print(self.meun.menu)
            option = input("请输入操作选项")  # input输入的都是字符串
            if option == '1':
                self.reg()
            elif option == '2':
                self.login()
            elif option == '3':
                # 查余额的时候 需要先登陆才行
                self.query_balance()
            elif option == '4':
                self.deposit()  # 存款  存款的时候必须是100的整数倍 还要判断用户是否登陆
            elif option == '5':
                self.withdraw()  # 取款
            elif option == '6':
                self.transfer()  # 转账
            elif option == '7':
                print("感谢你的使用")
                break
            else:
                print("菜单输入错误 请重新输入")

    def reg(self):
        while True:
            name = input("请输入用户名(注册)")
            for user in self.user_list:
                if name == user.name:
                    print("用户名已经存在,请重新输入")
                    break  # 跳出本次循序
            else:  # for 正常结束时 执行
                pw = input("请输入密码(注册)")
                if len(pw) < 6:
                    print("密码长度小于6,请重新输入")
                else:
                    # return False
                    print("注册成功 奖励3000元")
                    self.user_list.append(User(name,pw,3000))
                    break

    def login(self):
        ireturn = False  # 为了退出外层循序，内层循环退出的时候 将外层循环的标记进行修改   然后再判断外层循环的标记决定是否退出外层循环
        while True:
            uname = input("请输入用户名")
            upass = input("请输入密码")
            for user in self.user_list:
                if user.name == uname and user.passwd == upass:
                    print("恭喜你登陆成功")
                    ireturn = True
                    self.current_user = user
                    break
            else:
                print("密码或用户名错误，请重新输入")
                # uname = input("请输入用户名")
            if ireturn:
                break

    def query_balance(self):
        if self.current_user:
            print(f"欢迎{self.current_user.name}登陆系统，您的余额{self.current_user.balance}")
        else:
            print("请先登陆系统")
            self.login()

    def deposit(self):
        # step 1 判断用户是否登陆
        if self.current_user:
            money = input("欢迎存款,请输入存款金额")
            if money.isdigit() and money[-2:] == '00':
                self.current_user.balance += int(money)
                print(f"恭喜你存款成功,当前余额为{self.current_user.balance}")

            else:
                print("存款的金额有问题请重新存款")
        else:
            print("用户未登陆，请先登陆")
            self.login()
        # step 2 判断输入的金额是否符合要求(100倍数的整数)

    def withdraw(self):
        pass

    def transfer(self):
        pass


if __name__ == '__main__':
    bank = Bank()
    bank.option()

