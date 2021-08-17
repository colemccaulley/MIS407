def manyf(x, y=1, **kwargs):
    print("x = {}".format(x))
    print("y = {}".format(y))
    if 'a' in kwargs:
        print('a = {}'.format(kwargs['a']))
    if 'b' in kwargs:
        print('b = {}'.format(kwargs['b']))
    print(kwargs)


manyf(10)
manyf(10, 11)
manyf(x=10, y=11, a=12, b=134)
manyf(a=12, b=134, x=10, y=11)
