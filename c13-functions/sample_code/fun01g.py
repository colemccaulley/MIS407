# WARNING: This code is not supposed to work.
def manyf(x, y=1, *args):
    print("x = {}".format(x))
    print("y = {}".format(y))
    if 'a' in args:
        print('a = {}'.format(args['a']))
    if 'b' in args:
        print('b = {}'.format(args['b']))
    print(args)


manyf(10)
manyf(10, 11)
manyf(x=10, y=11, 12, 134)
