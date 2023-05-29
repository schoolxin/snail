print("{}And{}".format('hello', 'China'))
# 不按顺序，指定位置的输出位置
print("{1}And{0}".format('hello', 'China'))
print("{:.2f}".format(3.4455556))
# 占位符
print("%(name)sAnd%(age)d" % {"name": "hello", "age": 90})

age = 25
print(f"我今年{age}岁")
