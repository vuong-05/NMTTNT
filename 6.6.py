from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Game XO 6x6')
clicked = True
count = 0
win = False

# khai báo từng button thủ công
b1 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b2 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b3 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b4 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b5 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b6 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")

b7 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b8 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b9 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b10 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b11 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b12 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")

b13 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b14 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b15 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b16 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b17 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b18 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")

b19 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b20 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b21 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b22 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b23 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b24 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")

b25 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b26 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b27 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b28 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b29 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b30 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")

b31 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b32 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b33 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b34 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b35 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")
b36 = Button(root, text=" ", font=("Helvetica", 20), height=2, width=5, bg="SystemButtonFace")

buttons = [
    b1, b2, b3, b4, b5, b6,
    b7, b8, b9, b10, b11, b12,
    b13, b14, b15, b16, b17, b18,
    b19, b20, b21, b22, b23, b24,
    b25, b26, b27, b28, b29, b30,
    b31, b32, b33, b34, b35, b36
]

def disableButtons():
    for button in buttons:
        button.config(state=DISABLED)

def checkWinner():
    global win
    win = False

    # kiểm tra hàng ngang
    for r in range(6):
        for c in range(2):
            line = [buttons[r * 6 + c + i] for i in range(5)]
            if all(b["text"] == "x" for b in line):
                for b in line:
                    b.config(bg="#80ffaa")
                win = True
                messagebox.showinfo("OX Game", "Player 1 WINNER!!")
                disableButtons()
                return
            elif all(b["text"] == "o" for b in line):
                for b in line:
                    b.config(bg="#80ffaa")
                win = True
                messagebox.showinfo("OX Game", "Player 2 WINNER!!")
                disableButtons()
                return

    # kiểm tra cột dọc
    for c in range(6):
        for r in range(2):
            line = [buttons[(r + i) * 6 + c] for i in range(5)]
            if all(b["text"] == "x" for b in line):
                for b in line:
                    b.config(bg="#80ffaa")
                win = True
                messagebox.showinfo("OX Game", "Player 1 WINNER!!")
                disableButtons()
                return
            elif all(b["text"] == "o" for b in line):
                for b in line:
                    b.config(bg="#80ffaa")
                win = True
                messagebox.showinfo("OX Game", "Player 2 WINNER!!")
                disableButtons()
                return

    # kiểm tra chéo chính
    for r in range(2):
        for c in range(2):
            line = [buttons[(r + i) * 6 + (c + i)] for i in range(5)]
            if all(b["text"] == "x" for b in line):
                for b in line:
                    b.config(bg="#80ffaa")
                win = True
                messagebox.showinfo("OX Game", "Player 1 WINNER!!")
                disableButtons()
                return
            elif all(b["text"] == "o" for b in line):
                for b in line:
                    b.config(bg="#80ffaa")
                win = True
                messagebox.showinfo("OX Game", "Player 2 WINNER!!")
                disableButtons()
                return

    # kiểm tra chéo phụ
    for r in range(2):
        for c in range(4, 6):
            line = [buttons[(r + i) * 6 + (c - i)] for i in range(5)]
            if all(b["text"] == "x" for b in line):
                for b in line:
                    b.config(bg="#80ffaa")
                win = True
                messagebox.showinfo("OX Game", "Player 1 WINNER!!")
                disableButtons()
                return
            elif all(b["text"] == "o" for b in line):
                for b in line:
                    b.config(bg="#80ffaa")
                win = True
                messagebox.showinfo("OX Game", "Player 2 WINNER!!")
                disableButtons()
                return

def b_click(btn):
    global clicked, count
    if btn["text"] == " " and not win:
        if clicked:
            btn["text"] = "x"
            clicked = False
        else:
            btn["text"] = "o"
            clicked = True
        count += 1
        checkWinner()
        if count == 36 and not win:
            messagebox.showinfo("OX Game", "It's a Tie!")

# đặt từng button thủ công theo grid và gán command
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=0, column=3)
b5.grid(row=0, column=4)
b6.grid(row=0, column=5)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
b10.grid(row=1, column=3)
b11.grid(row=1, column=4)
b12.grid(row=1, column=5)

b13.grid(row=2, column=0)
b14.grid(row=2, column=1)
b15.grid(row=2, column=2)
b16.grid(row=2, column=3)
b17.grid(row=2, column=4)
b18.grid(row=2, column=5)

b19.grid(row=3, column=0)
b20.grid(row=3, column=1)
b21.grid(row=3, column=2)
b22.grid(row=3, column=3)
b23.grid(row=3, column=4)
b24.grid(row=3, column=5)

b25.grid(row=4, column=0)
b26.grid(row=4, column=1)
b27.grid(row=4, column=2)
b28.grid(row=4, column=3)
b29.grid(row=4, column=4)
b30.grid(row=4, column=5)

b31.grid(row=5, column=0)
b32.grid(row=5, column=1)
b33.grid(row=5, column=2)
b34.grid(row=5, column=3)
b35.grid(row=5, column=4)
b36.grid(row=5, column=5)

# gán command cho từng button
b1.config(command=lambda: b_click(b1))
b2.config(command=lambda: b_click(b2))
b3.config(command=lambda: b_click(b3))
b4.config(command=lambda: b_click(b4))
b5.config(command=lambda: b_click(b5))
b6.config(command=lambda: b_click(b6))

b7.config(command=lambda: b_click(b7))
b8.config(command=lambda: b_click(b8))
b9.config(command=lambda: b_click(b9))
b10.config(command=lambda: b_click(b10))
b11.config(command=lambda: b_click(b11))
b12.config(command=lambda: b_click(b12))

b13.config(command=lambda: b_click(b13))
b14.config(command=lambda: b_click(b14))
b15.config(command=lambda: b_click(b15))
b16.config(command=lambda: b_click(b16))
b17.config(command=lambda: b_click(b17))
b18.config(command=lambda: b_click(b18))

b19.config(command=lambda: b_click(b19))
b20.config(command=lambda: b_click(b20))
b21.config(command=lambda: b_click(b21))
b22.config(command=lambda: b_click(b22))
b23.config(command=lambda: b_click(b23))
b24.config(command=lambda: b_click(b24))

b25.config(command=lambda: b_click(b25))
b26.config(command=lambda: b_click(b26))
b27.config(command=lambda: b_click(b27))
b28.config(command=lambda: b_click(b28))
b29.config(command=lambda: b_click(b29))
b30.config(command=lambda: b_click(b30))

b31.config(command=lambda: b_click(b31))
b32.config(command=lambda: b_click(b32))
b33.config(command=lambda: b_click(b33))
b34.config(command=lambda: b_click(b34))
b35.config(command=lambda: b_click(b35))
b36.config(command=lambda: b_click(b36))

root.mainloop()