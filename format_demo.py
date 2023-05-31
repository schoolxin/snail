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
r2 = random.randint(5,10)
print(r2)
