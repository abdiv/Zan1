def dmu(a, b):
    d = not((b[3:5] >= a[3:5]) and (b[0:2] >= a[0:2]))
    print(int(b[-4::]) - int(a[-4::]) - int(d))


dmu('12.12.1987', '11.12.2019')

