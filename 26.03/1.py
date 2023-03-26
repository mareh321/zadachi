def sdsd():
    a = eval(input())
    b = int(input())
    c = ''
    d = 0
    for i in range(b):
        if i - d == len(a):

            d += len(a)
            c += str(a[i - d])
        else:
            c += str(a[i - d])
    print(c)


sdsd()
