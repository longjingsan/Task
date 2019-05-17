# 继承的语法
# 在python中，任何类都有一个共同的父类叫object

class Person():
    name = "NoName"
    age = 18
    __score = 0  # 考试成绩是秘密，只要自己知道
    _petname = "sec"  # 小名，是保护的，子类可以用，但不能公用

    def __init__(self):
        print("l'm a Person")
    def sleep(self):
        print("Sleeping ... ...")
    def work(self):
        print("make some money")

# 父类写在括号内
class Teacher(Person):
    def __init__(self):
        print("l'm a init in Teacher")

    # __init__就是构造函数
    # 每次实例化的时候，第一个被自动的调用
    # 因为主要工作是进行初始化，所以得名

    teacher_id = "9527"
    name = "yingzi"
    def make_test(self):
        print("attention")
    def work(self):
        # 扩充父类的功能只需要调用父类相应的函数
        Person.work(self)
        # Person.work(self)
        # 扩充父类的另一种方法
        # super代表得到父类
       #  super().work()

        self.make_test()

class Women(Person):
    pass
w = Women()


t = Teacher()
print(t.name)
# 受保护不能外部访问，为啥这里可以
print(t._petname)

# 私有访问问题
# 公开访问私有变量，报错
# print(t.__score)

t.sleep()
print(t.teacher_id)
t.make_test()

# 实例化的时候，括号内的参数需要跟构造函数参数匹配
t1 = Teacher()

# 实例话的时候，自动调用了Dog的构造函数
t1.work()

print(type(super))
help(super)






