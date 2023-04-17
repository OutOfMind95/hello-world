def f(*args, **kwargs):
    print("Positional: ", args, end=" ")
    print("Keyword: ", kwargs)


f(100, 50, 25, galleons=100, sickles=50, knuts=25)
