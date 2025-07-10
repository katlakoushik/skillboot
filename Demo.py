class Demo:
    def show(self,a=None,b=None,c=None):
        if a and b and c:
            print(a,b,c)
        elif a and b:
            print(a,b)
        elif a:
            print(a)
        else:
            print("0")
obj=Demo()
obj.show()
obj.show(1,2,3)
obj.show(1,2)
obj.show(1)