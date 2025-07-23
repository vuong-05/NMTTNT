from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('OX Game 8x8')
# Nguoi choi 1 [X] di truoc, Nguoi choi 2 [O] tiep theo sau
clicked = True
count = 0
buttons = []  # Ma trận lưu các nút 8x8

def disableButtons():
    # Vô hiệu hóa tất cả các nút (64 nút cho bàn 8x8)
    for row in range(8):
        for col in range(8):
            buttons[row][col].config(state=DISABLED)

def checkWinner():
    global win
    win = False
    
    # Kiểm tra hàng ngang (8 hàng)
    for row in range(8):
        for col in range(4):  # Chỉ cần kiểm tra đến cột 4 vì cần 5 ô liên tiếp
            if (buttons[row][col]["text"] == "X" and 
                buttons[row][col+1]["text"] == "X" and 
                buttons[row][col+2]["text"] == "X" and 
                buttons[row][col+3]["text"] == "X" and 
                buttons[row][col+4]["text"] == "X"):
                # Đánh dấu các ô thắng
                for i in range(5):
                    buttons[row][col+i].config(bg="#80ffaa")
                win = True
                messagebox.showinfo("OX Game", "Player 1 WINNER!!")
                disableButtons()
                return
            
    # Kiểm tra hàng dọc (8 cột)
    for col in range(8):
        for row in range(4):  # Chỉ cần kiểm tra đến hàng 4
            if (buttons[row][col]["text"] == "X" and 
                buttons[row+1][col]["text"] == "X" and 
                buttons[row+2][col]["text"] == "X" and 
                buttons[row+3][col]["text"] == "X" and 
                buttons[row+4][col]["text"] == "X"):
                # Đánh dấu các ô thắng
                for i in range(5):
                    buttons[row+i][col].config(bg="#80ffaa")
                win = True
                messagebox.showinfo("OX Game", "Player 1 WINNER!!")
                disableButtons()
                return
    
    # Kiểm tra đường chéo chính (từ trái trên sang phải dưới)
    for row in range(4):
        for col in range(4):
            if (buttons[row][col]["text"] == "X" and 
                buttons[row+1][col+1]["text"] == "X" and 
                buttons[row+2][col+2]["text"] == "X" and 
                buttons[row+3][col+3]["text"] == "X" and 
                buttons[row+4][col+4]["text"] == "X"):
                # Đánh dấu các ô thắng
                for i in range(5):
                    buttons[row+i][col+i].config(bg="#80ffaa")
                win = True
                messagebox.showinfo("OX Game", "Player 1 WINNER!!")
                disableButtons()
                return
    
    # Kiểm tra đường chéo phụ (từ phải trên sang trái dưới)
    for row in range(4):
        for col in range(4, 8):
            if (buttons[row][col]["text"] == "X" and 
                buttons[row+1][col-1]["text"] == "X" and 
                buttons[row+2][col-2]["text"] == "X" and 
                buttons[row+3][col-3]["text"] == "X" and 
                buttons[row+4][col-4]["text"] == "X"):
                # Đánh dấu các ô thắng
                for i in range(5):
                    buttons[row+i][col-i].config(bg="#80ffaa")
                win = True
                messagebox.showinfo("OX Game", "Player 1 WINNER!!")
                disableButtons()
                return
    
    # Tương tự kiểm tra cho người chơi O
    for row in range(8):
        for col in range(4):
            if (buttons[row][col]["text"] == "O" and 
                buttons[row][col+1]["text"] == "O" and 
                buttons[row][col+2]["text"] == "O" and 
                buttons[row][col+3]["text"] == "O" and 
                buttons[row][col+4]["text"] == "O"):
                for i in range(5):
                    buttons[row][col+i].config(bg="#80ffaa")
                win = True
                messagebox.showinfo("OX Game", "Player 2 WINNER!!")
                disableButtons()
                return
    
    for col in range(8):
        for row in range(4):
            if (buttons[row][col]["text"] == "O" and 
                buttons[row+1][col]["text"] == "O" and 
                buttons[row+2][col]["text"] == "O" and 
                buttons[row+3][col]["text"] == "O" and 
                buttons[row+4][col]["text"] == "O"):
                for i in range(5):
                    buttons[row+i][col].config(bg="#80ffaa")
                win = True
                messagebox.showinfo("OX Game", "Player 2 WINNER!!")
                disableButtons()
                return
    
    for row in range(4):
        for col in range(4):
            if (buttons[row][col]["text"] == "O" and 
                buttons[row+1][col+1]["text"] == "O" and 
                buttons[row+2][col+2]["text"] == "O" and 
                buttons[row+3][col+3]["text"] == "O" and 
                buttons[row+4][col+4]["text"] == "O"):
                for i in range(5):
                    buttons[row+i][col+i].config(bg="#80ffaa")
                win = True
                messagebox.showinfo("OX Game", "Player 2 WINNER!!")
                disableButtons()
                return
    
    for row in range(4):
        for col in range(4, 8):
            if (buttons[row][col]["text"] == "O" and 
                buttons[row+1][col-1]["text"] == "O" and 
                buttons[row+2][col-2]["text"] == "O" and 
                buttons[row+3][col-3]["text"] == "O" and 
                buttons[row+4][col-4]["text"] == "O"):
                for i in range(5):
                    buttons[row+i][col-i].config(bg="#80ffaa")
                win = True
                messagebox.showinfo("OX Game", "Player 2 WINNER!!")
                disableButtons()
                return

# Hàm checkDraw nếu hòa nhau
def checkDraw():
    global count, win
    if count == 64 and win == False:  # 8x8 = 64 ô
        messagebox.showerror("OX Game", "DRAW!!")
        start()

# Xác định các nút mà Người chơi 1 hoặc Người chơi 2 đã nhấp vào 
def buttonClicked(row, col):
    global clicked, count
    if buttons[row][col]["text"] == " " and clicked == True:
        buttons[row][col]["text"] = "X"
        clicked = False
        count += 1
        checkWinner()
        checkDraw()
    elif buttons[row][col]["text"] == " " and clicked == False:
        buttons[row][col]["text"] = "O"
        clicked = True
        count += 1
        checkWinner()
        checkDraw()
    else:
        messagebox.showerror("OX Game", "LỖI!! Vui lòng chọn lại")

# Bắt đầu hoặc chơi lại
def start():
    global buttons, clicked, count
    clicked = True
    count = 0
    
    # Xóa các nút cũ nếu có
    for widget in root.winfo_children():
        if isinstance(widget, Button):
            widget.destroy()
    
    # Tạo ma trận nút 8x8
    buttons = []
    for row in range(8):
        button_row = []
        for col in range(8):
            btn = Button(root, text=" ", font=("Helvetica", 16), height=2, width=4, 
                         bg="SystemButtonFace", command=lambda r=row, c=col: buttonClicked(r, c))
            btn.grid(row=row, column=col)
            button_row.append(btn)
        buttons.append(button_row)

# Tạo menu trò chơi
gameMenu = Menu(root)
root.config(menu=gameMenu)

# Tạo menu tùy chọn trò chơi
optionMenu = Menu(gameMenu, tearoff=False)
gameMenu.add_cascade(label="Options", menu=optionMenu)
optionMenu.add_command(label="Restart Game", command=start)

# Bắt đầu trò chơi
start()
root.mainloop()