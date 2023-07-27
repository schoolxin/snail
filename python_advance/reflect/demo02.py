x = 10


def func():
    y = 20
    a = eval('x+y')
    print("a:", a)

    b = eval('x+y', {'x': 1, 'y': 2})

    print("b:", b)

    print("x:", x, "y:", y)

    c = eval('x+y', {'x': 1, 'y': 2},{'x': 100, 'z': 200})

    print("c:", c)

    print("x:", x, "y:", y)

func()
