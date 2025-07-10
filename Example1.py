class Example:
    def greet(self, name=None):
        if name:
            print(f"Hello, {name}")
        else:
            print("Hello")

obj = Example()
obj.greet("Zara")  
obj.greet()