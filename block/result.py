import tkinter
import random

index = 0
timer = 0
score = 0
next_kitty = 0
tsugi = 0
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

def draw_neko():
    cvs.delete("NEKO")
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x * 72 + 60, y * 72 + 60, image=img_neko[neko[y][x]], tag="NEKO")

def check_neko():
    for y in range(10):
        for x in range(8):
            check[y][x] = neko[y][x]

    for y in range(1, 9):
        for x in range(8):
            if check[y][x] > 0:
                if check[y - 1][x] == check[y][x] and check[y + 1][x] == check[y][x]:
                    neko[y - 1][x] = 7
                    neko[y][x] = 7
                    neko[y + 1][x] = 7

    for y in range(10):
        for x in range(1, 7):
            if check[y][x] > 0:
                if check[y][x - 1] == check[y][x] and check[y][x + 1] == check[y][x]:
                    neko[y][x - 1] = 7
                    neko[y][x] = 7
                    neko[y][x + 1] = 7

    for y in range(1, 9):
        for x in range(1, 7):
            if check[y][x] > 0:
                if check[y - 1][x - 1] == check[y][x] and check[y + 1][x + 1] == check[y][x]:
                    neko[y - 1][x - 1] = 7
                    neko[y][x] = 7
                    neko[y + 1][x + 1] = 7
                if check[y + 1][x - 1] == check[y][x] and check[y - 1][x + 1] == check[y][x]:
                    neko[y + 1][x - 1] = 7
                    neko[y][x] = 7
                    neko[y - 1][x + 1] = 7

def sweep_neko(): # 발자국 삭제 함수 
    num = 0
    for y in range(10):
        for x in range(8):
            if neko[y][x] == 7:
                neko[y][x] = 0
                num = num + 1
    return num

def drop_neko(): # 고양이 낙하 함수 
    flg = False
    for y in range(8, -1, -1):
        for x in range(8):
            if neko[y][x] != 0 and neko[y + 1][x] == 0:
                neko[y + 1][x] = neko[y][x]
                neko[y][x] = 0
                flg = True
    return flg

def over_neko(): # 가장 윗줄 도달 여부 확인
    for x in range(8):
        if neko[0][x] > 0:
            return True
    return False

def set_neko(): # 가장 윗줄에 고양이 무작위 배치 
    for x in range(8):
        neko[0][x] = random.randint(0, 6)

def draw_txt(txt, x, y, siz, col, tg):
    fnt = ("Times New Roman", siz, "bold") # 그림자가 있는 텍스트 ( 타이틀 화면 ) 
    cvs.create_text(x + 2, y + 2, text=txt, fill="black", font=fnt, tag=tg)
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg)

def game_main():
    global index, timer, score, next_kitty
    global cursor_x, cursor_y, mouse_c
    global tsugi
    if index == 0:  # 타이틀 로고
        draw_txt("야옹야옹", 312, 240, 100, "violet", "TITLE")
        draw_txt("Click to start.", 312, 560, 50, "orange", "TITLE")
        index = 1
        mouse_c = 0
    elif index == 1:  # 타이틀 화면 / 시작 대기
        if mouse_c == 1:
            for y in range(10):
                for x in range(8):
                    neko[y][x] = 0
            mouse_c = 0
            score = 0
            tsugi = 0
            cursor_x = 0
            cursor_y = 0
            set_neko()
            draw_neko()
            cvs.delete("TITLE")
            index = 2
    elif index == 2:  # 낙하
        if drop_neko() == False:
            index = 3
        draw_neko()
    elif index == 3:  # 나란히 놓였는가
        check_neko()
        draw_neko()
        index = 4
    elif index == 4:  # 나란히 놓인 고양이가 있다면 삭제
        sc = sweep_neko()
        score = score + sc * 10
        if sc > 0:
            index = 2
        else:
            if over_neko() == False:
                tsugi = random.randint(1, 6)
                index = 5
            else:
                index = 6
                timer = 0
        draw_neko()
    elif index == 5:  # 마우스 입력 대기
        if 24 <= mouse_x and mouse_x < 24 + 72 * 8 and 24 <= mouse_y and mouse_y < 24 + 72 * 10:
            cursor_x = int((mouse_x - 24) / 72)
            cursor_y = int((mouse_y - 24) / 72)
            if mouse_c == 1:
                mouse_c = 0
                set_neko()
                neko[cursor_y][cursor_x] = tsugi
                tsugi = 0
                index = 2
        cvs.delete("CURSOR")
        cvs.create_image(cursor_x * 72 + 60, cursor_y * 72 + 60, image=cursor, tag="CURSOR")
        draw_neko()
    elif index == 6:  # 게임 오버
        timer = timer + 1
        if timer == 1:
            draw_txt("GAME OVER", 312, 348, 60, "red", "OVER")
        if timer == 50:
            cvs.delete("OVER")
            index = 0
    cvs.delete("INFO")
    draw_txt("SCORE " + str(score), 160, 60, 32, "blue", "INFO")
    if tsugi > 0:
        cvs.create_image(752, 128, image=img_neko[tsugi], tag="INFO")
    root.after(100, game_main)

root = tkinter.Tk()
root.title("낙하 퍼즐 '야옹야옹'")
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
    tkinter.PhotoImage(file="neko_niku.png")
]
cvs.create_image(456, 384, image=bg)
game_main()
root.mainloop()
