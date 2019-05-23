# import p01 # 导入就相当于把被导入的代码从头到尾执行了一次
           #因此最后的print函数里面的内容也会被执行
class Student():
    def __init__(self, name = "Noname", age = 20):
        self.name = name
        self.age = age

    def say(self):
        print("my name is {}".format(self.name))

def sayHello():
    print("hello,welcome to there")

print("this is a word")

stu1 = Student("yingzi",29)

stu1.say()

sayHello()
'''stu1 = p01.Student("yingzi",29)

stu1.say()

p01.sayHello()'''