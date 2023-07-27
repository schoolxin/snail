x = 1

y = exec('x=1+1')  # exec中的代码块中的变量可以在外部进行使用 exec 不会返回值

print("x", x, "y", y)

fn = '''a=[]\na.append(100)\na.append(200)\nprint(a[0])'''

exec(fn)
# print(a)
print(a)

c = "mydict={'name':'woniu'}"

exec(c)
print(type(mydict))
