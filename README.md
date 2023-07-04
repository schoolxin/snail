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
# random 模块
* random.random() 返回[0.0,1.0)之间的浮点数
* random.randint(5,10) 返回[5,10] 之间的整数
* random.randrange(5,10) 返回[5,10) 之间的整数
* random.uniform(5,10) 返回[5,10] 之间的浮点数
* random.choice([1,2,3,4,56,4]) # 从列表中选一个数
* random.shuffle(a) # 随机打乱元素的顺序 没有返回值 原地打乱
* r :在字符串前面加上一个r，就会将该字符串的所有转义字符变成普通字符




# 列表
* 用[]将列表中的元素括起来即可
* '+' 号 将两个列表拼接在一起
* in 用于判断一个元素是否在列表中就可以用该语法
* 求列表中的最大值 max(列表)
* list 方法可以将字符串转化为列表
* append 在列表末尾添加一个元素
* count 统计某个元素在列表中出现的次数
* extend 在列表的末尾一次性添加一个序列的值
* index 从列表中找出第一次匹配的位置
* insert 可以指定插入的位置
* pop 默认删除列表最后一个元素 也可以指定index位置进行删除 并返回删除的元素
* remove 指定要删除元素的值 删除元素 只删除指定元素的第一个
* del  把整个列表进行删除 删除整个变量空间
* reverse 将列表进行逆序输出 
* sort 对列表进行排序 sort方法可以接收一个key参数

# 可变数据类型和不可变数据类型
> 不可变：当数据类型的变量的值发生变化时，它对应的内存地址也发生变化 id(变量)
* 字符串 数值型 元组 是不可变
> 可变： 当数据类型的变量的值发生变化时，它对应的内存地址不发生变化 id(变量)
* list 集合用大括号定义{}  字典 是可变 

# 元组

> 用小括号定义

> 如果元组只有一个元素的时候，必须在元素后面加一个逗号

# 集合
* 使用大括号定义
* 集合是一个无序且不重复的元素集，集合里面的元素没有位置坐标的,只能用不可变的数据类型作为集合的元素
* 注意1：所有可变的数据类型是不可以哈希的
* set 强制类型转化方法，可以将一个可迭代类型转化为集合(set)
* 集合还支持数学中的关于集合的操作，比如交集  并集  差集

# 字典
* 使用大括号定义 键值对之前用冒号间隔  每个元素之间用逗号隔开
* 如果字典中出现两个相同键的值，则后面的键会替换之前同名键的值
* 值可以是任意数据类型 但是键必须是不可变
> 字典的基本操作
* 直接使用{} 大括号定义
* 访问字典  dic1.get("name") 和 dic1["name"] 都可以
* dic[键值] 如果指定的键存在则修改 如果不存在则新增
* 删除字典中的键值对  del dic1['name']  dic1.pop('name') dic1.popitem() 随机删除一个“键-值”对
* 如果元素与元素之间有映射关系，那么最好选用字典作为容器 如果元素与元素之间没有任何关系相互是独立的最好使用列表
* 求字典的长度：使用len方法 len(字典)
* 字典的深拷贝使用copy方法
* fromkeys 创建一个新的字典，以序列中的元素作为键，也可以指定一个val作为字典的值，如果没有指定val，则默认为None
* in 判断键是否在字典中或者对字典进行循环
* items() 取出字典中所有的键值对
* keys values 分别取出字典中所有的键和 值
* setdefault 可以根据指定键取对应的值，如果键不存在，会添加新键到字典中并将值设定为默认值
* update 使用字典更新字典中的值，如果键不存在怎新增一个新的键 d5.update({"name":"eee",'height':100})
* pop 根据指定的键去删除字典中的键值对 如果键不存在就会报错 可以给一个默认值 不报错
* popitem 随机地删除字典中的一个键值对，一般时字典的末尾开始删
# 条件
* 在python中以下值表示假值：'',None 0 () [] {} False
* break 退出循环   continue 忽略当前项，继续循环
* 当使用break和continue时 只能作用于当前循环，如果当前循环还有父循环，则无法从父循环中continue或break
* 循环中的else  当循环体正常执行完之后，中途没有被break，则else 语句块会执行

# 函数
* 函数默认会返回一个None值(即在不写return语句的前提下)
### 函数的参数
* 就是用户在调用函数时从外部传入的变量，我们可以在函数中任意使用这些变量来进行操作
* 位置参数：调用函数时 根据函数定义时的参数位置来传递参数值，这个就是位置参数
* 关键字参数：通过键值对的形式 进行传递参数 这样可以让函数更加清晰，避免了参数顺序的要求 foo(name="lishi",age=100)
> 如果函数中定义了关键字参数，关键字参数后面就不能再跟位置参数了
* 默认参数，是在函数定义时 给参数的默认值，在调用函数时可以传参数的值也可以不传参数的值,所有位置参数必须出现在默认参数前面
* 可变参数：在函数定义时，可以不确定参数的个数，在调用函数传参时根据实际情况传递n个参数
> foo1(*args,**kwargs) 调用是所有的位置参数被args接收(是一个元组的形式)，所有的关键字参数被kwargs接收(是一个字典形式参数)
* 形参：定义函数时定义的参数
* 实参：调用函数时传递的参数
* 形参和实参的关系：
> 如果传入的实参是可变的参数，那么形参的改变将会影响实参的值，也就是说实参会跟着形参变化 相当于把实参的地址给了形参，
> 实参和形参指向了同一个地址中的值
> 
> 如果传入的实参是一个不可变的参数，那么形参的改变将不会影响实参的值 赋值时 相当于把实参的值拷贝了一份给形参

* 变量作用域
* 全部变量，作用于全局，在所有的函数中都可以访问
* 局部变量，也叫本地变量，是指在函数内定义的，只能在函数内部访问
* 如果函数内部的局部变量跟全局变量同名，则局部变量会暂时屏蔽全部变量 如果必须要对全局变量进行重新赋值(=)的时候
那么在函数内部将全局变量再用global进行声明一次,但是如果全局变量是一个可变数据类型，那么函数内部的修改将会影响全局变量的值
* 匿名函数
> 使用关键字lambda关键字来创建,lambda函数能接收任意数量的参数，但是只能写一句表达式，如果一个函数超过一个表达式，
> 则不适合使用匿名函数来定义，建议使用普通函数
> 
> 语法：lambda[参数]:表达式
> 
> 使用规则：
>>定义的是单行函数，如果一个函数比较复杂，应该定义为普通函数
>>
>>可以接受多个参数 不用写return 关键字 也可以没有参数

# 模块
* 所有自我包含并且有组织的代码片段就叫模块，在python的表现形式为一个py文件，其中文件名就是该模块的名字

# 包
* 包是一个有层次的文件目录结构，它定义了有n个模块或n个子包组成的python应用程序的执行环境
* 包在python中就是一个包含_init_.py文件的目录
* 如何区分一个py文件是被作为主程序还是作为一个模块被导入到其他文件中使用？
> 要区分一个文件是作为主程序还是被作为模块被导入，需要用到模块的属性__name__
> 
> 如果一个文件作为主程序执行的时候__name__的值为__main__ 如果是被作为模块导入的话,__name__的值为文件名比如py2导入py1 那么__name__值为py1

# pip 管理第三方库
* pip list 查看所有的第三方包
* pip install 安装第三方包
* pip install -i 指定安装时 使用的镜像服务器 比如国内的镜像 install -i https://pypi.douban.com/simple<包名>
* pip install -U<包名> 升级第三方包
* pip uninstall 卸载指定的第三方包
* pip freeze 查看当前python环境中所有已安装的包的版本 可以生成一个requirements文件(pip freeze > requirements.txt)
* pip install  -r 根据requirements文件快速安装第三方包
* 使用 requirements.txt文件 快速的将其他环境备份出来的包安装到现在的环境中(pip install  -r requirements.txt)
* 上面的操作可以保证多个环境中的包版本一致
* pip show <包名> 查看具体包的信息
* pip search<包名> 根据指定的关键字搜索包

# 面向对象
### 类和对象
* 类：就是一群具有相同特征或行为的事物的总称
* 对象：就是类的实例
* 使用dir 查看对象的属性和方法
* 定义类时，如果同一个方法被定义多次 最后的一个会覆盖前面的
* 其中的定义方法中的self  是在对象调用方法时作为隐式的第一个参数进行传递
### 常见的方法类型 
*  __init__ (self):初始化方法 (对象==实例)
> 不需要显示调用，在初始化一个类(创建对象实例时) 会由python自动调用
> 
> 初始化 方法并不是必须的，一般只有在需要定义对象属性时或者继承父类时需要定义__init__ 方法，如果没有定义默认调用终极父类的__init__方法
* 实例化方法(方法的第一个参数为self)
> 实例方法只能通过对象调用
>
> 实例方法在定义时必须以self作为第一个参数
> 
> 使用方法在调用时，不需要传入self参数，调用这个方法的实例对象会被隐式传入该方法作为self参数的值
* 类方法
> 可以直接由类名进行调用，也可以通过实例调用
>
> 类方法定义时必须使用@classmethod 装饰器进行修饰
> 
> 所有的类方法的第一个参数必须是cls
> 
> 不能访问实例属性，只能访问类属性
* 静态方法
> 只能通过@staticmethod装饰器装饰
> 
> 静态方法既不能访问实例属性也不能访问类属性
> 
> 可以通过类名直接调用也可以通过对象调用

### 属性的种类
* 实例属性
> 跟实例绑定，只能由对象进行访问，不能直接通过类名访问 通过实例方法也可以进行访问
* 类属性
> 不能实例绑定，可以通过类名或实例访问，也可以在实例方法中访问类属性

## 面向对象的三大特征
### 继承
* 创建一个类A ，如果这个类A继承自类B，那么A类会获取到类B所有的属性和方法，类B叫做类A的父类，类A叫做类B的子类
> 优势：提高代码的重用性，我们不用一遍又一遍的敲那些方法和属性，可以直接通过继承让子类马上获取到父类所有方法和属性
> 可以方便地扩展自己的属性
> 
> 当时用继承时，我们必须注意初始化方法__init__的行为：
>>* 如果子类没有定义自己的初始化方法，则父类的初始化方法被自动调用,如果要实例化子类对象，必须要传入父类初始化方法对应的参数，否则会报错
>> 
>>* 如果子类定义了自己的初始化方法，而在子类中没有显示调用父类的初始化方法，则父类的所有属性都不会被初始化,一般情况下，
如果我们需要在子类中定义子类的属性，则需要在子类中定义初始化方法，否则一般不需要定义自己的初始化方法
>>* 如果子类中定义了自己的属性，在子类中显示调用父类初始化方法，则子类和父类的属性都会被初始化(super().__init__(name,age,stuno)或者Student.__init__(self,name,age,stuno))

* 重新父类的方法
> 如果在子类中定义了跟父类同名的方法，则子类的方法将覆盖父类的方法，实现子类方法的自定义

### 封装
* 概念：将对象的状态信息隐藏在对象内部，不允许外部程序直接访问对象内部的信息，只能通过该类提供的方法来实现对类内部信息进行操作和访问
* 封装的目的
>* 隐藏类的实现细节
>* 让使用者，只能通过预先定义好的方法来访问类内部的信息，我们可以在这些访问方法上加上一些控制逻辑，限制对属性的不合理访问
>* 可以进行数据检查，从而有利于保护对象信息的完整性
>* 便于修改，提高代码的可维护性
* 封装的两个含义：1.将该隐藏的隐藏起来，2.该暴露的暴露出来
* 将对象的属性和实现细节隐藏起来
* 把接口方法暴露出来，让方法来控制对这些属性的安全访问和操作
* 在python代码中实现属性和方法隐藏，在定义的时候使用双下滑线开头__

### 多态
* 如果一个类的子类重写了父类的某一个方法，那么在其他函数取调用这个类的方法时，将根据传入的子类不同呈现出不同的行为
* 父类对象不是一个子类对象，一个子类对象就是一个父类对象 可以使用isinstance 加以判断 python动态语言 鸭子模型 看起来像鸭子
* 多态实现了著名的开闭原则  开放：允许任意新增的Animal类型； 闭：对修改封闭，不需要修改依赖Animal类型的say方法


# 文件操作

## 文本文件操作
* f = open(文件路径,mode='r') 打开一个文件，f.close() 关闭文件
* 文件的打开模式：
* 
>* r 只读 不主动生产文件，从文件的开头开始读 rb 已二进制的形式打开
>* r+ 读写 不主动生成文件，从文件的开头读或写
>* w 只写，主动生成文件，清空以前的内容，从头开始写
>* w+ 写读，主动生成文件，清空以前的内容，从头开始写
>* a 追加只写，主动生成文件，从文件末尾开始写内容
>* a+ 追加读写，主动生成文件，从文件末尾开始读或写内容

## 读取数据
* read 按照指定的字符数进行读取，或者一次性读取所有的数据 只适合读取比较小的文件或者不需要单独对每行文字进行处理。
* readline：按行读取文件内容，每次读取一行
* readlines: 一次性读取文件所有内容并以列表的形式返回，每行文字就是列表中的一个元素
* with：通过with关键字使用上下文管理器来直接操作文件,可以让上下文管理器帮助我们自动管理文件，不需要我们手动通过代码关闭文件
>* with open(r'file\python.txt', encoding='UTF-8') as f 其中的f 是一个可迭代的对象(文件的一行行数据)
## 写入文件
>* 文件指针：seek(offset,whence):主要是移动文件指针,让文件指针移动到指定的位置，offset指针的偏移量，whence指偏离相对位置，whence为0时是相对于文件开头
位置进行位移，当whence为1时，是相对于当前位置进行位移，当whence为2时，是相对于文件末尾位置进行位移。只有当文件是以文本模式打开whence只能取0值，也就是只能
相对于文件开头进行位移，如果以*b模式打开的话 whence 可以去 0 1 2
* tell 获取当前指针的位置.
* write：可以直接写入字符串或以二进制模式写入字节串，一般我们保存图片、音频等二进制文件时需要使用write方法
* writelines:可以接受一个可迭代的对象，比如一个列表或元组，把要写入文件的内容放入到元组或列表中即可
