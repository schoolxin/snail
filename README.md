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
* 
