import tkinter
import random

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1

neko = []
check = []
for i in range(10):
    neko.append([0, 0, 0, 0, 0, 0, 0, 0])
    check.append([0, 0, 0, 0, 0, 0, 0, 0])

def draw_neko(): #고양이 표시 함수 
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x*72+60, y*72+60, image=img_neko[neko[y][x]], tag="NEKO")

def check_neko(): # 가로, 세로, 대각선 3개인지 확인하는 함수 
    for y in range(10):
        for x in range(8):
            check[y][x] = neko[y][x]

    for y in range(1, 9):
        for x in range(8):
            if check[y][x] > 0: 
                if check[y-1][x] == check[y][x] and check[y+1][x] == check[y][x]: # 위아래 
                    neko[y-1][x] = 7
                    neko[y][x] = 7
                    neko[y+1][x] = 7

    for y in range(10):
        for x in range(1, 7):
            if check[y][x] > 0:
                if check[y][x-1] == check[y][x] and check[y][x+1] == check[y][x]: #좌우 
                    neko[y][x-1] = 7
                    neko[y][x] = 7
                    neko[y][x+1] = 7

    for y in range(1, 9):
        for x in range(1, 7):
            if check[y][x] > 0:
                if check[y-1][x-1] == check[y][x] and check[y+1][x+1] == check[y][x]: 왼쪽 대각선
                    neko[y-1][x-1] = 7
                    neko[y][x] = 7
                    neko[y+1][x+1] = 7
                if check[y+1][x-1] == check[y][x] and check[y-1][x+1] == check[y][x]: 오른쪽 대각선
                    neko[y+1][x-1] = 7
                    neko[y][x] = 7
                    neko[y-1][x+1] = 7

# 연속된 같은 값을 찾을 때 사용하는 배열(check)과 결과를 저장하는 배열(neko)을 분리하여 사용하므로, 
# 한번에 모든 방향(가로, 세로, 대각선)의 연속 값을 확인하고 변경할 수 있다.
def game_main():
    global cursor_x, cursor_y, mouse_c
    if 660 <= mouse_x and mouse_x < 840 and 100 <= mouse_y and mouse_y < 160 and mouse_c == 1:
        mouse_c = 0
        check_neko() # 고양이 연결 확인 함수 
    if 24 <= mouse_x and mouse_x < 24+72*8 and 24 <= mouse_y and mouse_y < 24+72*10:
        cursor_x = int((mouse_x-24)/72)
        cursor_y = int((mouse_y-24)/72)
        if mouse_c == 1:
            mouse_c = 0
            neko[cursor_y][cursor_x] = random.randint(1, 2)
    cvs.delete("CURSOR")
    cvs.create_image(cursor_x*72+60, cursor_y*72+60, image=cursor, tag="CURSOR")
    cvs.delete("NEKO")
    draw_neko()
    root.after(100, game_main)

root = tkinter.Tk()
root.title("세로, 가로, 대각선으로 3개 나란히 놓였는가")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()

bg = tkinter.PhotoImage(file="neko_bg.png")
cursor = tkinter.PhotoImage(file="neko_cursor.png")
img_neko = [
    None,
    tkinter.PhotoImage(file="neko1.png"),
    tkinter.PhotoImage(file="neko2.png"),
    tkinter.PhotoImage(file="neko3.png"),
    tkinter.PhotoImage(file="neko4.png"),
    tkinter.PhotoImage(file="neko5.png"),
    tkinter.PhotoImage(file="neko6.png"),
    tkinter.PhotoImage(file="neko_niku.png")]


cvs.create_image(456, 384, image=bg)
cvs.create_rectangle(660, 100, 840, 160, fill="white")
cvs.create_text(750, 130, text="테스트", fill="red", font=("Times New Roman", 30))
game_main()
root.mainloop()
