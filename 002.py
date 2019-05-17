# 多继承的例子
# 子类可以直接拥有父类的属性和方法，私有属性和方法除外
class Fish():
    def __init__(self, name):
        self.name = name

    def swim(self):
        print("i am swimming......")


class Bird():
    def __init__(self, name):
        self.name = name

    def fly(self):
        print("I am flying.....")


class Person():
    def __init__(self, name):
        self.name = name

    def work(self):
        print("Working........")


# 单继承的例子
class Student(Person):
    def __init__(self, name):
        self.name = name


stu = Student("yueyue")
stu.work()


# 多继承的例子
class SuperMan(Person, Bird, Fish):
    def __init__(self, name):
        self.name = name


class SwimMan(Person, Fish):
    def __init__(self, name):
        self.name = name


s = SuperMan("yueyue") # 因为构造函数里面要求有参数
s.fly()
s.swim()

class Student(Person):
    def __init__(self,name):
        print("my name is {}.format(name)")
stu = Student("yingzi")
stu.work()


# 菱形继承
class A():
    pass
class B(A):
    pass
class C(A):
    pass

class D(B,C):
    pass


