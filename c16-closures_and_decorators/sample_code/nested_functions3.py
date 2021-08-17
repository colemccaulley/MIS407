def f(x):
    def g(y):
        return(y**x)
    return(g)
sqr = f(2)
print(sqr(3))
sqrt = f(1/2)
print(sqrt(9))
cube = f(3)
print(cube(3))
cubert = f(1/3)
print(cubert(27))
