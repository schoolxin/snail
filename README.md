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
* 











