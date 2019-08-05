print("hello ")
# zheshi k29那个案例
import math
import random
def line():
    #定义一个空字符串用于拼接字母
    strm = " "
    #前四个字符用asc码进行转换
    for i in range(4):
        num1 = random.randrange(97,123)
        strm1 = chr(num1)
        strm = strm +strm1

    for i in range(8):
        num2 = random.randrange(0,10)
        strm = strm + str(num2)
    print(strm)
    return strm
num = input("请输入一个三位数")
random_num = random.randrange(100,1000)
if num.isdigit() and 100<=int(num)<=999:
    num = int(num)
    random_num = int(random_num)
    if num > random_num:
        bai = num // 100
        shi =( num % 100 )//10
        ge = num % 10
        print("百十个位分别是{}和{}和{}".format(bai,shi,ge))
    if num == random_num:
        print("你中奖啦")
        print(random_num)
    if num < random_num:#将120个字符保存到文本文件中
                        # 原则是每一条字符串的长度为12，单独占一行，并且前四个是字符，后面8个是数字
                        # 通过ascii码转换，chr（）函数和ord（）
        for i in range(10):

            raw = line()
            # print(raw)
            print(random_num)
            with open("strm.txt","a") as f:
                f.write(raw + "\n")


else:
    print("请重新输入")




