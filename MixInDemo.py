class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        super().__init__() # 1
        print('A.__init__')

class B(Base):
    def __init__(self):
        super().__init__() # 2
        print('B.__init__')

class C(A,B):
    def __init__(self):
        super().__init__() 
        print('C.__init__')

if __name__ == '__main__':
    c = C()