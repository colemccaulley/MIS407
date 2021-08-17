def manyf(x, y=1, *args):
    print("x = {}".format(x))
    print("y = {}".format(y))
    if len(args) > 0:
        print("the rest  = {}".format(list(args)))


manyf(10)
manyf(10, 11)
manyf(10, 11, 12, 134)
