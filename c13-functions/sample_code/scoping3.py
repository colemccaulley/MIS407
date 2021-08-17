
def outer_function():
    # "nonlocal a" will result in the inner_function call having
    # nothing to bind to in this nonlocal (but nonglobal) context, and
    # thus will generate and error.

    # remove the nonolocal statement here to make code work
    # (and see what the difference is versus global)
    nonlocal a
    a = 20

    def inner_function():
        nonlocal a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a =', a)
