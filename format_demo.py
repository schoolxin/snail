# print("{}And{}".format('hello', 'China'))
# # 不按顺序，指定位置的输出位置
# print("{1}And{0}".format('hello', 'China'))
# print("{:.2f}".format(3.4455556))
# # 占位符
# print("%(name)sAnd%(age)d" % {"name": "hello", "age": 90})
#
# age = 25
# print(f"我今年{age}岁")
#
# import math
#
# print(math.ceil(10.2))
# print(math.ceil(-10.2))
#
# print(math.floor(10.2))
# print(math.floor(-10.2))
# print(math.fsum([x for x in range(101)]))
# a = math.sqrt(10)
#
# print("{a:.2f}".format(a=a))
# print(f"{a:.2f}")
# print(f"{a:.4f}")
# print("%.4f" % a)
import random

r1 = random.random()
print(r1)
r2 = random.randint(5, 10)  # [5,10]
print(r2)
r3 = random.randrange(5, 10)  # [5,10)
print(r3)

r4 = random.uniform(5, 10)  # [5,10] 浮点数
print(r4)
random.choice([1, 2, 3, 4, 56, 4])  # 从列表中选一个数
a = [1, 2, 3, 4, 5]
random.shuffle(a)  # 原地改变
print(a)

s = random.sample(a, 2)
print(s)

str = "helloworld"
print(str[0:len(str)])
print("++++++++++++++++++++++++++++++++++")
str1 = "欢迎大家来到蜗牛学院学习python课程"
r1 = str1[-3:-8:-1]
# r2 = str1[-8:-2:-1]
print(r1)
print(r2)
