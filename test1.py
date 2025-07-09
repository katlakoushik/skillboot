def divv(a,b):
    if b == 0:
        try:
            return a/b
        except ZeroDivisionError:
            print("ZeroDivisionError")
    else:
         print(a/b)
a=int(input())
b=int(input())
divv(a,b)
