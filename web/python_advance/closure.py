func_list = []
for i in range(3):
    def deco(i):

        def myfunc(a):
            return i + a
        return myfunc

    func_list.append(deco(i))

for f in func_list:
    print(f(1))
