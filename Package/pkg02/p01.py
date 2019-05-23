# 包含一个学生类，
# 包含一个sayHello函数
# 一个打印语句
class Student():
    def __init__(self, name = "Noname", age = 20):
        self.name = name
        self.age = age

    def say(self):
        print("my name is {}".format(self.name))

def sayHello():
    print("hello,welcome to there")


# 此判断语句建议一直作为程序的入口，即程序第一句被执行的代码
if __name__ == '__main__':#该文件真正被本身执行的时候是作为主文件
   #作为被导入文件是它就不是主文件，name就不是main
    print("this is a word")
#上面这行语句最好不要有，因为导入一次执行一次