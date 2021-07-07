# ch11: 클래스
 
class MyClass:
    sharedName="hi"
    def __init__(self, name):
        print("called MyClass init")
        self.name = name
    def foo(self):
        print("My name is %s"%self.name)
    def mob():
        print("Class Function")

a = MyClass("Hong")
b = MyClass("Sung")

a.foo()
b.foo()

print(MyClass.sharedName)
MyClass.mob()
MyClass.foo(a)