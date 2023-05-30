# 虚拟环境的创建
## 创建的方式
> 使用virtualenv
> 使用virtualenvwrapper
* virtualenvwrapper作为virtualenv功能的扩展，可以统一管理虚拟环境(将虚拟环境放到WORKON_HOME目录下)，并且方便我们用单个命令切换不同的虚拟环境、查看所有已创建的虚拟环境等
* pip install virtualenvwrapper-win
* 使用virtualenvwrapper 中的workon 命令进行创建和查看虚拟环境

## 格式化
> 占位符 %d %s %f 等格式化方式
* print("%(name)sAnd%(age)d" % {"name": "hello","age": 90})
> format 格式化
* 按顺序的格式输出
> print("{}And{}".format('hello', 'China'))

> print("{:.2f}".format(3.4455556))
* 不按顺序，指定位置的输出位置
> print("{1}And{0}".format('hello', 'China'))

> 用f标示进行格式化输出
> 
> age = 25 print(f"我今年{age}岁")

# 数据类型
> // 地板除的结果是比商小的最大整数 eg：8//-5 = 2 8//5=1
* math模块
> ceil 返回大于等于x的最小整数 如果x是整数则返回x本身
> 
> fabs：返回浮点型的绝对值
> 
> floor 返回小于或等于x的最大的整数，如果x是一个整数则返回x本身
> 
> fsum 主要用于列表或其他可迭代类型的变量，对里面的每个元素求和 返回的值是浮点数
> 
> 





























