import tkinter


if __name__ =='__main__':
    root_window = tkinter.Tk()

    root_window.title("飞机大战")
    root_window.resizable(width=False, height=False)

    #创建画布
    window_canvas = tkinter.Canvas(root_window, width=480, height=600)
    window_canvas.pack()

    # 在画布上添加一个图片
    # 三个步骤；定义图片的位置，创建photoimage对象，利用create——image函数把图片画上去

    bg_img_name = "图片路径"
    bg_img = tkinter.PhotoImage(file=bg_img_name)
    # tags的作用是，以后我们使用创建好的image可以通过tags使用
    window_canvas.create_image(240, 300, anchor=tkinter.CENTER,
                               image=bg_img, tags="bg")
    # 画上一个小蜜蜂
    bee_img_name = "图片路径"
    bee_img = tkinter.PhotoImage(file=bee_img_name)
    # tags的作用是，以后我们使用创建好的image可以通过tags使用
    window_canvas.create_image(240, 300, anchor=tkinter.CENTER,
                               image=bee_img, tags="bee")





    root_window.mainloop()
