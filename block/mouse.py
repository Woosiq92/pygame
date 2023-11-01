import tkinter

mouse_x = 0
mouse_y = 0
mouse_c = 0

def mouse_move(e): # 마우스 이동 
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e): # 마우스 클릭
    global mouse_c
    mouse_c = 1

def mouse_release(e): # 마우스 해제 
    global mouse_c
    mouse_c = 0

def game_main():
    fnt = ("Times New Roman", 30)
    txt = "mouse({},{}){}".format(mouse_x, mouse_y, mouse_c)
    cvs.delete("TEST")
    cvs.create_text(456, 384, text=txt, fill="black", font=fnt, tag="TEST")
    root.after(100, game_main)

root = tkinter.Tk()
root.title("마우스 입력")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
root.bind("<ButtonRelease>", mouse_release)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()
game_main()
root.mainloop()
