import  tkinter
import time
import random  as rd
'''
蜜蜂从上往下走
可以通过每个键盘左右控制

'''


step = 0 #用于计算小飞机一共走了多少步
direction = (1,1)

x = 0
y = 10
def set_right(e):
    global x
    x += 20

def set_left(e):
    global x
    x -= 20


root_window = tkinter.Tk()
root_window.title("北京图灵学院")

root_window.bind('<key-left>',set_left)
root_window.bind('<key-right>',set_right)
root_wiondow.resizable(width=False, height=False)

#创建画布
window_canvas = tkinter.Canvas(root_window,
                               width=480,
                               height=600)
window_canvas.pack()

def main():
    #创建
   #创建开始界面

   #创建小飞机

   #注意坐标的位置

   #让小飞机动起来的函数叫
   ap_move()
   tkinter,mianloop()
def ap_move():
    global step
    global x
    global y

    y +=20
    print(x,y)
    window_canvas.move("sp",x,y)

    step +=1
    window_canvas.after(1000, ap_move)



#root_window.mainloop()
if __name__=='__main__':
    main()