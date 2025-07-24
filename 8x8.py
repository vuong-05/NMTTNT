from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Game XO 8x8')
# Nguoi choi 1 [X] di truoc, Nguoi choi 2 [O] tiep theo sau
clicked = True
count = 0
win = False

def disableButtons():
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)
    button10.config(state=DISABLED)
    button11.config(state=DISABLED)
    button12.config(state=DISABLED)
    button13.config(state=DISABLED)
    button14.config(state=DISABLED)
    button15.config(state=DISABLED)
    button16.config(state=DISABLED)
    button17.config(state=DISABLED)
    button18.config(state=DISABLED)
    button19.config(state=DISABLED)
    button20.config(state=DISABLED)
    button21.config(state=DISABLED)
    button22.config(state=DISABLED)
    button23.config(state=DISABLED)
    button24.config(state=DISABLED)
    button25.config(state=DISABLED)
    button26.config(state=DISABLED)
    button27.config(state=DISABLED)
    button28.config(state=DISABLED)
    button29.config(state=DISABLED)
    button30.config(state=DISABLED)
    button31.config(state=DISABLED)
    button32.config(state=DISABLED)
    button33.config(state=DISABLED)
    button34.config(state=DISABLED)
    button35.config(state=DISABLED)
    button36.config(state=DISABLED)
    button37.config(state=DISABLED)
    button38.config(state=DISABLED)
    button39.config(state=DISABLED)
    button40.config(state=DISABLED)
    button41.config(state=DISABLED)
    button42.config(state=DISABLED)
    button43.config(state=DISABLED)
    button44.config(state=DISABLED)
    button45.config(state=DISABLED)
    button46.config(state=DISABLED)
    button47.config(state=DISABLED)
    button48.config(state=DISABLED)
    button49.config(state=DISABLED)
    button50.config(state=DISABLED)
    button51.config(state=DISABLED)
    button52.config(state=DISABLED)
    button53.config(state=DISABLED)
    button54.config(state=DISABLED)
    button55.config(state=DISABLED)
    button56.config(state=DISABLED)
    button57.config(state=DISABLED)
    button58.config(state=DISABLED)
    button59.config(state=DISABLED)
    button60.config(state=DISABLED)
    button61.config(state=DISABLED)
    button62.config(state=DISABLED)
    button63.config(state=DISABLED)
    button64.config(state=DISABLED)

def checkWinner():
    global win
    win = False
    
    # Điều kiện thắng
    # X Win
    # cot 1
    if button1["text"] == "x" and button2["text"] == "x" and button3["text"] == "x" and button4["text"] == "x" and button5["text"] == "x":
        button1.config(bg="#80ffaa")
        button2.config(bg="#80ffaa")
        button3.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        button5.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button2["text"] == "x" and button3["text"] == "x" and button4["text"] == "x" and button5["text"] == "x" and button6["text"] == "x":
        button2.config(bg="#80ffaa")
        button3.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        button5.config(bg="#80ffaa")
        button6.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button3["text"] == "x" and button4["text"] == "x" and button5["text"] == "x" and button6["text"] == "x" and button7["text"] == "x":
        button3.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        button5.config(bg="#80ffaa")
        button6.config(bg="#80ffaa")
        button7.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button4["text"] == "x" and button5["text"] == "x" and button6["text"] == "x" and button7["text"] == "x" and button8["text"] == "x":
        button4.config(bg="#80ffaa")
        button5.config(bg="#80ffaa")
        button6.config(bg="#80ffaa")
        button7.config(bg="#80ffaa")
        button8.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    
    # cot 2
    elif button9["text"] == "x" and button10["text"] == "x" and button11["text"] == "x" and button12["text"] == "x" and button13["text"] == "x":
        button9.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button10["text"] == "x" and button11["text"] == "x" and button12["text"] == "x" and button13["text"] == "x" and button14["text"] == "x":
        button10.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button11["text"] == "x" and button12["text"] == "x" and button13["text"] == "x" and button14["text"] == "x" and button15["text"] == "x":
        button11.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button12["text"] == "x" and button13["text"] == "x" and button14["text"] == "x" and button15["text"] == "x" and button16["text"] == "x":
        button12.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        button16.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    # cot 3
    elif button17["text"] == "x" and button18["text"] == "x" and button19["text"] == "x" and button20["text"] == "x" and button21["text"] == "x":
        button17.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button18["text"] == "x" and button19["text"] == "x" and button20["text"] == "x" and button21["text"] == "x" and button22["text"] == "x":
        button18.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button19["text"] == "x" and button20["text"] == "x" and button21["text"] == "x" and button22["text"] == "x" and button23["text"] == "x":
        button19.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button20["text"] == "x" and button21["text"] == "x" and button22["text"] == "x" and button23["text"] == "x" and button24["text"] == "x":
        button20.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()

    # cot 4
    elif button25["text"] == "x" and button26["text"] == "x" and button27["text"] == "x" and button28["text"] == "x" and button29["text"] == "x":
        button25.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button26["text"] == "x" and button27["text"] == "x" and button28["text"] == "x" and button29["text"] == "x" and button30["text"] == "x":
        button26.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button27["text"] == "x" and button28["text"] == "x" and button29["text"] == "x" and button30["text"] == "x" and button31["text"] == "x":
        button27.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button28["text"] == "x" and button29["text"] == "x" and button30["text"] == "x" and button31["text"] == "x" and button32["text"] == "x":
        button28.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()

    # cot 5
    elif button33["text"] == "x" and button34["text"] == "x" and button35["text"] == "x" and button36["text"] == "x" and button37["text"] == "x":
        button33.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button34["text"] == "x" and button35["text"] == "x" and button36["text"] == "x" and button37["text"] == "x" and button38["text"] == "x":
        button34.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button35["text"] == "x" and button36["text"] == "x" and button37["text"] == "x" and button38["text"] == "x" and button39["text"] == "x":
        button35.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button36["text"] == "x" and button37["text"] == "x" and button38["text"] == "x" and button39["text"] == "x" and button40["text"] == "x":
        button36.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()

    # cot 6
    elif button41["text"] == "x" and button42["text"] == "x" and button43["text"] == "x" and button44["text"] == "x" and button45["text"] == "x":
        button41.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button42["text"] == "x" and button43["text"] == "x" and button44["text"] == "x" and button45["text"] == "x" and button46["text"] == "x":
        button42.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button43["text"] == "x" and button44["text"] == "x" and button45["text"] == "x" and button46["text"] == "x" and button47["text"] == "x":
        button43.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button44["text"] == "x" and button45["text"] == "x" and button46["text"] == "x" and button47["text"] == "x" and button48["text"] == "x":
        button44.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        button48.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()

    # cot 7
    elif button49["text"] == "x" and button50["text"] == "x" and button51["text"] == "x" and button52["text"] == "x" and button53["text"] == "x":
        button49.config(bg="#80ffaa")
        button50.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button50["text"] == "x" and button51["text"] == "x" and button52["text"] == "x" and button53["text"] == "x" and button54["text"] == "x":
        button50.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button51["text"] == "x" and button52["text"] == "x" and button53["text"] == "x" and button54["text"] == "x" and button55["text"] == "x":
        button51.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button52["text"] == "x" and button53["text"] == "x" and button54["text"] == "x" and button55["text"] == "x" and button56["text"] == "x":
        button52.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        button56.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()

    # cot 8
    elif button57["text"] == "x" and button58["text"] == "x" and button59["text"] == "x" and button60["text"] == "x" and button61["text"] == "x":
        button57.config(bg="#80ffaa")
        button58.config(bg="#80ffaa")
        button59.config(bg="#80ffaa")
        button60.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button58["text"] == "x" and button59["text"] == "x" and button60["text"] == "x" and button61["text"] == "x" and button62["text"] == "x":
        button58.config(bg="#80ffaa")
        button59.config(bg="#80ffaa")
        button60.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        button62.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button59["text"] == "x" and button60["text"] == "x" and button61["text"] == "x" and button62["text"] == "x" and button63["text"] == "x":
        button59.config(bg="#80ffaa")
        button60.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        button62.config(bg="#80ffaa")
        button63.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button60["text"] == "x" and button61["text"] == "x" and button62["text"] == "x" and button63["text"] == "x" and button64["text"] == "x":
        button60.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        button62.config(bg="#80ffaa")
        button63.config(bg="#80ffaa")
        button64.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    # O win
    # cot 1
    if button1["text"] == "o" and button2["text"] == "o" and button3["text"] == "o" and button4["text"] == "o" and button5["text"] == "o":
        button1.config(bg="#80ffaa")
        button2.config(bg="#80ffaa")
        button3.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        button5.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button2["text"] == "o" and button3["text"] == "o" and button4["text"] == "o" and button5["text"] == "o" and button6["text"] == "o":
        button2.config(bg="#80ffaa")
        button3.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        button5.config(bg="#80ffaa")
        button6.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button3["text"] == "o" and button4["text"] == "o" and button5["text"] == "o" and button6["text"] == "o" and button7["text"] == "o":
        button3.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        button5.config(bg="#80ffaa")
        button6.config(bg="#80ffaa")
        button7.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button4["text"] == "o" and button5["text"] == "o" and button6["text"] == "o" and button7["text"] == "o" and button8["text"] == "o":
        button4.config(bg="#80ffaa")
        button5.config(bg="#80ffaa")
        button6.config(bg="#80ffaa")
        button7.config(bg="#80ffaa")
        button8.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    
    # cot 2
    elif button9["text"] == "o" and button10["text"] == "o" and button11["text"] == "o" and button12["text"] == "o" and button13["text"] == "o":
        button9.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button10["text"] == "o" and button11["text"] == "o" and button12["text"] == "o" and button13["text"] == "o" and button14["text"] == "o":
        button10.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button11["text"] == "o" and button12["text"] == "o" and button13["text"] == "o" and button14["text"] == "o" and button15["text"] == "o":
        button11.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button12["text"] == "o" and button13["text"] == "o" and button14["text"] == "o" and button15["text"] == "o" and button16["text"] == "o":
        button12.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        button16.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    # cot 3
    elif button17["text"] == "o" and button18["text"] == "o" and button19["text"] == "o" and button20["text"] == "o" and button21["text"] == "o":
        button17.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button18["text"] == "o" and button19["text"] == "o" and button20["text"] == "o" and button21["text"] == "o" and button22["text"] == "o":
        button18.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button19["text"] == "o" and button20["text"] == "o" and button21["text"] == "o" and button22["text"] == "o" and button23["text"] == "o":
        button19.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button20["text"] == "o" and button21["text"] == "o" and button22["text"] == "o" and button23["text"] == "o" and button24["text"] == "o":
        button20.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    # cot 4
    elif button25["text"] == "o" and button26["text"] == "o" and button27["text"] == "o" and button28["text"] == "o" and button29["text"] == "o":
        button25.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button26["text"] == "o" and button27["text"] == "o" and button28["text"] == "o" and button29["text"] == "o" and button30["text"] == "o":
        button26.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button27["text"] == "o" and button28["text"] == "o" and button29["text"] == "o" and button30["text"] == "o" and button31["text"] == "o":
        button27.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button28["text"] == "o" and button29["text"] == "o" and button30["text"] == "o" and button31["text"] == "o" and button32["text"] == "o":
        button28.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    # cot 5
    elif button33["text"] == "o" and button34["text"] == "o" and button35["text"] == "o" and button36["text"] == "o" and button37["text"] == "o":
        button33.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button34["text"] == "o" and button35["text"] == "o" and button36["text"] == "o" and button37["text"] == "o" and button38["text"] == "o":
        button34.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button35["text"] == "o" and button36["text"] == "o" and button37["text"] == "o" and button38["text"] == "o" and button39["text"] == "o":
        button35.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button36["text"] == "o" and button37["text"] == "o" and button38["text"] == "o" and button39["text"] == "o" and button40["text"] == "o":
        button36.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    # cot 6
    elif button41["text"] == "o" and button42["text"] == "o" and button43["text"] == "o" and button44["text"] == "o" and button45["text"] == "o":
        button41.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button42["text"] == "o" and button43["text"] == "o" and button44["text"] == "o" and button45["text"] == "o" and button46["text"] == "o":
        button42.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button43["text"] == "o" and button44["text"] == "o" and button45["text"] == "o" and button46["text"] == "o" and button47["text"] == "o":
        button43.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button44["text"] == "o" and button45["text"] == "o" and button46["text"] == "o" and button47["text"] == "o" and button48["text"] == "o":
        button44.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        button48.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    # cot 7
    elif button49["text"] == "o" and button50["text"] == "o" and button51["text"] == "o" and button52["text"] == "o" and button53["text"] == "o":
        button49.config(bg="#80ffaa")
        button50.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button50["text"] == "o" and button51["text"] == "o" and button52["text"] == "o" and button53["text"] == "o" and button54["text"] == "o":
        button50.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button51["text"] == "o" and button52["text"] == "o" and button53["text"] == "o" and button54["text"] == "o" and button55["text"] == "o":
        button51.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button52["text"] == "o" and button53["text"] == "o" and button54["text"] == "o" and button55["text"] == "o" and button56["text"] == "o":
        button52.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        button56.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    # cot 8
    elif button57["text"] == "o" and button58["text"] == "o" and button59["text"] == "o" and button60["text"] == "o" and button61["text"] == "o":
        button57.config(bg="#80ffaa")
        button58.config(bg="#80ffaa")
        button59.config(bg="#80ffaa")
        button60.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button58["text"] == "o" and button59["text"] == "o" and button60["text"] == "o" and button61["text"] == "o" and button62["text"] == "o":
        button58.config(bg="#80ffaa")
        button59.config(bg="#80ffaa")
        button60.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        button62.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button59["text"] == "o" and button60["text"] == "o" and button61["text"] == "o" and button62["text"] == "o" and button63["text"] == "o":
        button59.config(bg="#80ffaa")
        button60.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        button62.config(bg="#80ffaa")
        button63.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button60["text"] == "o" and button61["text"] == "o" and button62["text"] == "o" and button63["text"] == "o" and button64["text"] == "o":
        button60.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        button62.config(bg="#80ffaa")
        button63.config(bg="#80ffaa")
        button64.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    # x win
    # hang 1
    elif button1["text"] == "x" and button9["text"] == "x" and button17["text"] == "x" and button25["text"] == "x" and button33["text"] == "x":
        button1.config(bg="#80ffaa")
        button9.config(bg="#80ffaa")
        button17.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button9["text"] == "x" and button17["text"] == "x" and button25["text"] == "x" and button33["text"] == "x" and button41["text"] == "x":
        button9.config(bg="#80ffaa")
        button17.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        button41.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button17["text"] == "x" and button25["text"] == "x" and button33["text"] == "x" and button41["text"] == "x" and button49["text"] == "x":
        button17.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        button41.config(bg="#80ffaa")
        button49.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button25["text"] == "x" and button33["text"] == "x" and button41["text"] == "x" and button49["text"] == "x" and button57["text"] == "x":
        button25.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        button41.config(bg="#80ffaa")
        button49.config(bg="#80ffaa")
        button57.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
        # hang 2
    elif button2["text"] == "x" and button10["text"] == "x" and button18["text"] == "x" and button26["text"] == "x" and button34["text"] == "x":
        button2.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button10["text"] == "x" and button18["text"] == "x" and button26["text"] == "x" and button34["text"] == "x" and button42["text"] == "x":
        button10.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button18["text"] == "x" and button26["text"] == "x" and button34["text"] == "x" and button42["text"] == "x" and button50["text"] == "x":
        button18.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        button50.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button26["text"] == "x" and button34["text"] == "x" and button42["text"] == "x" and button50["text"] == "x" and button58["text"] == "x":
        button26.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        button50.config(bg="#80ffaa")
        button58.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()

    # hang 3
    elif button3["text"] == "x" and button11["text"] == "x" and button19["text"] == "x" and button27["text"] == "x" and button35["text"] == "x":
        button3.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button11["text"] == "x" and button19["text"] == "x" and button27["text"] == "x" and button35["text"] == "x" and button43["text"] == "x":
        button11.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button19["text"] == "x" and button27["text"] == "x" and button35["text"] == "x" and button43["text"] == "x" and button51["text"] == "x":
        button19.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button27["text"] == "x" and button35["text"] == "x" and button43["text"] == "x" and button51["text"] == "x" and button59["text"] == "x":
        button27.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        button59.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()

    # hang 4
    elif button4["text"] == "x" and button12["text"] == "x" and button20["text"] == "x" and button28["text"] == "x" and button36["text"] == "x":
        button4.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button12["text"] == "x" and button20["text"] == "x" and button28["text"] == "x" and button36["text"] == "x" and button44["text"] == "x":
        button12.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button20["text"] == "x" and button28["text"] == "x" and button36["text"] == "x" and button44["text"] == "x" and button52["text"] == "x":
        button20.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button28["text"] == "x" and button36["text"] == "x" and button44["text"] == "x" and button52["text"] == "x" and button60["text"] == "x":
        button28.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button60.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()

    # hang 5
    elif button5["text"] == "x" and button13["text"] == "x" and button21["text"] == "x" and button29["text"] == "x" and button37["text"] == "x":
        button5.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button13["text"] == "x" and button21["text"] == "x" and button29["text"] == "x" and button37["text"] == "x" and button45["text"] == "x":
        button13.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button21["text"] == "x" and button29["text"] == "x" and button37["text"] == "x" and button45["text"] == "x" and button53["text"] == "x":
        button21.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button29["text"] == "x" and button37["text"] == "x" and button45["text"] == "x" and button53["text"] == "x" and button61["text"] == "x":
        button29.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()

    # hang 6
    elif button6["text"] == "x" and button14["text"] == "x" and button22["text"] == "x" and button30["text"] == "x" and button38["text"] == "x":
        button6.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button14["text"] == "x" and button22["text"] == "x" and button30["text"] == "x" and button38["text"] == "x" and button46["text"] == "x":
        button14.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button22["text"] == "x" and button30["text"] == "x" and button38["text"] == "x" and button46["text"] == "x" and button54["text"] == "x":
        button22.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button30["text"] == "x" and button38["text"] == "x" and button46["text"] == "x" and button54["text"] == "x" and button62["text"] == "x":
        button30.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        button62.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()

    # hang 7
    elif button7["text"] == "x" and button15["text"] == "x" and button23["text"] == "x" and button31["text"] == "x" and button39["text"] == "x":
        button7.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button15["text"] == "x" and button23["text"] == "x" and button31["text"] == "x" and button39["text"] == "x" and button47["text"] == "x":
        button15.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button23["text"] == "x" and button31["text"] == "x" and button39["text"] == "x" and button47["text"] == "x" and button55["text"] == "x":
        button23.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button31["text"] == "x" and button39["text"] == "x" and button47["text"] == "x" and button55["text"] == "x" and button63["text"] == "x":
        button31.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        button63.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()

    # hang 8
    elif button8["text"] == "x" and button16["text"] == "x" and button24["text"] == "x" and button32["text"] == "x" and button40["text"] == "x":
        button8.config(bg="#80ffaa")
        button16.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button16["text"] == "x" and button24["text"] == "x" and button32["text"] == "x" and button40["text"] == "x" and button48["text"] == "x":
        button16.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        button48.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button24["text"] == "x" and button32["text"] == "x" and button40["text"] == "x" and button48["text"] == "x" and button56["text"] == "x":
        button24.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        button48.config(bg="#80ffaa")
        button56.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button32["text"] == "x" and button40["text"] == "x" and button48["text"] == "x" and button56["text"] == "x" and button64["text"] == "x":
        button32.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        button48.config(bg="#80ffaa")
        button56.config(bg="#80ffaa")
        button64.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    # o win
        # hang 1
    elif button1["text"] == "o" and button9["text"] == "o" and button17["text"] == "o" and button25["text"] == "o" and button33["text"] == "o":
        button1.config(bg="#80ffaa")
        button9.config(bg="#80ffaa")
        button17.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button9["text"] == "o" and button17["text"] == "o" and button25["text"] == "o" and button33["text"] == "o" and button41["text"] == "o":
        button9.config(bg="#80ffaa")
        button17.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        button41.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button17["text"] == "o" and button25["text"] == "o" and button33["text"] == "o" and button41["text"] == "o" and button49["text"] == "o":
        button17.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        button41.config(bg="#80ffaa")
        button49.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button25["text"] == "o" and button33["text"] == "o" and button41["text"] == "o" and button49["text"] == "o" and button57["text"] == "o":
        button25.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        button41.config(bg="#80ffaa")
        button49.config(bg="#80ffaa")
        button57.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
        # hang 2
    elif button2["text"] == "o" and button10["text"] == "o" and button18["text"] == "o" and button26["text"] == "o" and button34["text"] == "o":
        button2.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button10["text"] == "o" and button18["text"] == "o" and button26["text"] == "o" and button34["text"] == "o" and button42["text"] == "o":
        button10.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button18["text"] == "o" and button26["text"] == "o" and button34["text"] == "o" and button42["text"] == "o" and button50["text"] == "o":
        button18.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        button50.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button26["text"] == "o" and button34["text"] == "o" and button42["text"] == "o" and button50["text"] == "o" and button58["text"] == "o":
        button26.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        button50.config(bg="#80ffaa")
        button58.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    # hang 3 O 
    elif button3["text"] == "o" and button11["text"] == "o" and button19["text"] == "o" and button27["text"] == "o" and button35["text"] == "o":
        button3.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button11["text"] == "o" and button19["text"] == "o" and button27["text"] == "o" and button35["text"] == "o" and button43["text"] == "o":
        button11.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button19["text"] == "o" and button27["text"] == "o" and button35["text"] == "o" and button43["text"] == "o" and button51["text"] == "o":
        button19.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button27["text"] == "o" and button35["text"] == "o" and button43["text"] == "o" and button51["text"] == "o" and button59["text"] == "o":
        button27.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        button59.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    # hang 4 
    elif button4["text"] == "o" and button12["text"] == "o" and button20["text"] == "o" and button28["text"] == "o" and button36["text"] == "o":
        button4.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button12["text"] == "o" and button20["text"] == "o" and button28["text"] == "o" and button36["text"] == "o" and button44["text"] == "o":
        button12.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button20["text"] == "o" and button28["text"] == "o" and button36["text"] == "o" and button44["text"] == "o" and button52["text"] == "o":
        button20.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button28["text"] == "o" and button36["text"] == "o" and button44["text"] == "o" and button52["text"] == "o" and button60["text"] == "o":
        button28.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button60.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    # hang 5 
    elif button5["text"] == "o" and button13["text"] == "o" and button21["text"] == "o" and button29["text"] == "o" and button37["text"] == "o":
        button5.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button13["text"] == "o" and button21["text"] == "o" and button29["text"] == "o" and button37["text"] == "o" and button45["text"] == "o":
        button13.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button21["text"] == "o" and button29["text"] == "o" and button37["text"] == "o" and button45["text"] == "o" and button53["text"] == "o":
        button21.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button29["text"] == "o" and button37["text"] == "o" and button45["text"] == "o" and button53["text"] == "o" and button61["text"] == "o":
        button29.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    # hang 6 
    elif button6["text"] == "o" and button14["text"] == "o" and button22["text"] == "o" and button30["text"] == "o" and button38["text"] == "o":
        button6.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button14["text"] == "o" and button22["text"] == "o" and button30["text"] == "o" and button38["text"] == "o" and button46["text"] == "o":
        button14.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button22["text"] == "o" and button30["text"] == "o" and button38["text"] == "o" and button46["text"] == "o" and button54["text"] == "o":
        button22.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button30["text"] == "o" and button38["text"] == "o" and button46["text"] == "o" and button54["text"] == "o" and button62["text"] == "o":
        button30.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        button62.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    # hang 7 
    elif button7["text"] == "o" and button15["text"] == "o" and button23["text"] == "o" and button31["text"] == "o" and button39["text"] == "o":
        button7.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button15["text"] == "o" and button23["text"] == "o" and button31["text"] == "o" and button39["text"] == "o" and button47["text"] == "o":
        button15.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button23["text"] == "o" and button31["text"] == "o" and button39["text"] == "o" and button47["text"] == "o" and button55["text"] == "o":
        button23.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button31["text"] == "o" and button39["text"] == "o" and button47["text"] == "o" and button55["text"] == "o" and button63["text"] == "o":
        button31.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        button63.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()

    # hang 8 
    elif button8["text"] == "o" and button16["text"] == "o" and button24["text"] == "o" and button32["text"] == "o" and button40["text"] == "o":
        button8.config(bg="#80ffaa")
        button16.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button16["text"] == "o" and button24["text"] == "o" and button32["text"] == "o" and button40["text"] == "o" and button48["text"] == "o":
        button16.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        button48.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button24["text"] == "o" and button32["text"] == "o" and button40["text"] == "o" and button48["text"] == "o" and button56["text"] == "o":
        button24.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        button48.config(bg="#80ffaa")
        button56.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button32["text"] == "o" and button40["text"] == "o" and button48["text"] == "o" and button56["text"] == "o" and button64["text"] == "o":
        button32.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        button48.config(bg="#80ffaa")
        button56.config(bg="#80ffaa")
        button64.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    
    # chéo
    # X win
    elif button1["text"] == "x" and button10["text"] == "x" and button19["text"] == "x" and button28["text"] == "x" and button37["text"] == "x":
        button1.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button10["text"] == "x" and button19["text"] == "x" and button28["text"] == "x" and button37["text"] == "x" and button46["text"] == "x":
        button10.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button19["text"] == "x" and button28["text"] == "x" and button37["text"] == "x" and button46["text"] == "x" and button55["text"] == "x":
        button19.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button28["text"] == "x" and button37["text"] == "x" and button46["text"] == "x" and button55["text"] == "x" and button64["text"] == "x":
        button28.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        button64.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button2["text"] == "x" and button11["text"] == "x" and button20["text"] == "x" and button29["text"] == "x" and button38["text"] == "x":
        button2.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button11["text"] == "x" and button20["text"] == "x" and button29["text"] == "x" and button38["text"] == "x" and button47["text"] == "x":
        button11.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button20["text"] == "x" and button29["text"] == "x" and button38["text"] == "x" and button47["text"] == "x" and button56["text"] == "x":
        button20.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        button56.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button3["text"] == "x" and button12["text"] == "x" and button21["text"] == "x" and button30["text"] == "x" and button39["text"] == "x":
        button3.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button12["text"] == "x" and button21["text"] == "x" and button30["text"] == "x" and button39["text"] == "x" and button48["text"] == "x":
        button12.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button48.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button4["text"] == "x" and button13["text"] == "x" and button22["text"] == "x" and button31["text"] == "x" and button40["text"] == "x":
        button4.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button9["text"] == "x" and button18["text"] == "x" and button27["text"] == "x" and button36["text"] == "x" and button45["text"] == "x":
        button9.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button18["text"] == "x" and button27["text"] == "x" and button36["text"] == "x" and button45["text"] == "x" and button54["text"] == "x":
        button18.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button27["text"] == "x" and button36["text"] == "x" and button45["text"] == "x" and button54["text"] == "x" and button63["text"] == "x":
        button27.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        button63.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button17["text"] == "x" and button26["text"] == "x" and button35["text"] == "x" and button44["text"] == "x" and button53["text"] == "x":
        button17.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button26["text"] == "x" and button35["text"] == "x" and button44["text"] == "x" and button53["text"] == "x" and button62["text"] == "x":
        button26.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button62.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button25["text"] == "x" and button34["text"] == "x" and button43["text"] == "x" and button52["text"] == "x" and button61["text"] == "x":
        button25.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button5["text"] == "x" and button12["text"] == "x" and button19["text"] == "x" and button26["text"] == "x" and button33["text"] == "x":
        button5.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button6["text"] == "x" and button13["text"] == "x" and button20["text"] == "x" and button27["text"] == "x" and button34["text"] == "x":
        button6.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button13["text"] == "x" and button20["text"] == "x" and button27["text"] == "x" and button34["text"] == "x" and button41["text"] == "x":
        button13.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button41.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button7["text"] == "x" and button14["text"] == "x" and button21["text"] == "x" and button28["text"] == "x" and button35["text"] == "x":
        button7.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button14["text"] == "x" and button21["text"] == "x" and button28["text"] == "x" and button35["text"] == "x" and button42["text"] == "x":
        button14.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button21["text"] == "x" and button28["text"] == "x" and button35["text"] == "x" and button42["text"] == "x" and button49["text"] == "x":
        button21.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        button49.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button8["text"] == "x" and button15["text"] == "x" and button22["text"] == "x" and button29["text"] == "x" and button36["text"] == "x":
        button8.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button15["text"] == "x" and button22["text"] == "x" and button29["text"] == "x" and button36["text"] == "x" and button43["text"] == "x":
        button15.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button22["text"] == "x" and button29["text"] == "x" and button36["text"] == "x" and button43["text"] == "x" and button50["text"] == "x":
        button22.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button50.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button29["text"] == "x" and button36["text"] == "x" and button43["text"] == "x" and button50["text"] == "x" and button57["text"] == "x":
        button29.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button50.config(bg="#80ffaa")
        button57.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button16["text"] == "x" and button23["text"] == "x" and button30["text"] == "x" and button37["text"] == "x" and button44["text"] == "x":
        button16.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button23["text"] == "x" and button30["text"] == "x" and button37["text"] == "x" and button44["text"] == "x" and button51["text"] == "x":
        button23.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button30["text"] == "x" and button37["text"] == "x" and button44["text"] == "x" and button51["text"] == "x" and button58["text"] == "x":
        button30.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        button58.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button24["text"] == "x" and button31["text"] == "x" and button38["text"] == "x" and button45["text"] == "x" and button52["text"] == "x":
        button24.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button31["text"] == "x" and button38["text"] == "x" and button45["text"] == "x" and button52["text"] == "x" and button59["text"] == "x":
        button31.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button59.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif button32["text"] == "x" and button39["text"] == "x" and button46["text"] == "x" and button53["text"] == "x" and button60["text"] == "x":
        button32.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button60.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    
        # O win
    elif button1["text"] == "o" and button10["text"] == "o" and button19["text"] == "o" and button28["text"] == "o" and button37["text"] == "o":
        button1.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button10["text"] == "o" and button19["text"] == "o" and button28["text"] == "o" and button37["text"] == "o" and button46["text"] == "o":
        button10.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button19["text"] == "o" and button28["text"] == "o" and button37["text"] == "o" and button46["text"] == "o" and button55["text"] == "o":
        button19.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button28["text"] == "o" and button37["text"] == "o" and button46["text"] == "o" and button55["text"] == "o" and button64["text"] == "o":
        button28.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button55.config(bg="#80ffaa")
        button64.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button2["text"] == "o" and button11["text"] == "o" and button20["text"] == "o" and button29["text"] == "o" and button38["text"] == "o":
        button2.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button11["text"] == "o" and button20["text"] == "o" and button29["text"] == "o" and button38["text"] == "o" and button47["text"] == "o":
        button11.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button20["text"] == "o" and button29["text"] == "o" and button38["text"] == "o" and button47["text"] == "o" and button56["text"] == "o":
        button20.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button47.config(bg="#80ffaa")
        button56.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button3["text"] == "o" and button12["text"] == "o" and button21["text"] == "o" and button30["text"] == "o" and button39["text"] == "o":
        button3.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button12["text"] == "o" and button21["text"] == "o" and button30["text"] == "o" and button39["text"] == "o" and button48["text"] == "o":
        button12.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button48.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button4["text"] == "o" and button13["text"] == "o" and button22["text"] == "o" and button31["text"] == "o" and button40["text"] == "o":
        button4.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button40.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button9["text"] == "o" and button18["text"] == "o" and button27["text"] == "o" and button36["text"] == "o" and button45["text"] == "o":
        button9.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button18["text"] == "o" and button27["text"] == "o" and button36["text"] == "o" and button45["text"] == "o" and button54["text"] == "o":
        button18.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button27["text"] == "o" and button36["text"] == "o" and button45["text"] == "o" and button54["text"] == "o" and button63["text"] == "o":
        button27.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button54.config(bg="#80ffaa")
        button63.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button17["text"] == "o" and button26["text"] == "o" and button35["text"] == "o" and button44["text"] == "o" and button53["text"] == "o":
        button17.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button26["text"] == "o" and button35["text"] == "o" and button44["text"] == "o" and button53["text"] == "o" and button62["text"] == "o":
        button26.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button62.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button25["text"] == "o" and button34["text"] == "o" and button43["text"] == "o" and button52["text"] == "o" and button61["text"] == "o":
        button25.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button61.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button5["text"] == "o" and button12["text"] == "o" and button19["text"] == "o" and button26["text"] == "o" and button33["text"] == "o":
        button5.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button6["text"] == "o" and button13["text"] == "o" and button20["text"] == "o" and button27["text"] == "o" and button34["text"] == "o":
        button6.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button13["text"] == "o" and button20["text"] == "o" and button27["text"] == "o" and button34["text"] == "o" and button41["text"] == "o":
        button13.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button41.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button7["text"] == "o" and button14["text"] == "o" and button21["text"] == "o" and button28["text"] == "o" and button35["text"] == "o":
        button7.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button14["text"] == "o" and button21["text"] == "o" and button28["text"] == "o" and button35["text"] == "o" and button42["text"] == "o":
        button14.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button21["text"] == "o" and button28["text"] == "o" and button35["text"] == "o" and button42["text"] == "o" and button49["text"] == "o":
        button21.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button42.config(bg="#80ffaa")
        button49.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button8["text"] == "o" and button15["text"] == "o" and button22["text"] == "o" and button29["text"] == "o" and button36["text"] == "o":
        button8.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button15["text"] == "o" and button22["text"] == "o" and button29["text"] == "o" and button36["text"] == "o" and button43["text"] == "o":
        button15.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button22["text"] == "o" and button29["text"] == "o" and button36["text"] == "o" and button43["text"] == "o" and button50["text"] == "o":
        button22.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button50.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button29["text"] == "o" and button36["text"] == "o" and button43["text"] == "o" and button50["text"] == "o" and button57["text"] == "o":
        button29.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")
        button43.config(bg="#80ffaa")
        button50.config(bg="#80ffaa")
        button57.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button16["text"] == "o" and button23["text"] == "o" and button30["text"] == "o" and button37["text"] == "o" and button44["text"] == "o":
        button16.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button23["text"] == "o" and button30["text"] == "o" and button37["text"] == "o" and button44["text"] == "o" and button51["text"] == "o":
        button23.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button30["text"] == "o" and button37["text"] == "o" and button44["text"] == "o" and button51["text"] == "o" and button58["text"] == "o":
        button30.config(bg="#80ffaa")
        button37.config(bg="#80ffaa")
        button44.config(bg="#80ffaa")
        button51.config(bg="#80ffaa")
        button58.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button24["text"] == "o" and button31["text"] == "o" and button38["text"] == "o" and button45["text"] == "o" and button52["text"] == "o":
        button24.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button31["text"] == "o" and button38["text"] == "o" and button45["text"] == "o" and button52["text"] == "o" and button59["text"] == "o":
        button31.config(bg="#80ffaa")
        button38.config(bg="#80ffaa")
        button45.config(bg="#80ffaa")
        button52.config(bg="#80ffaa")
        button59.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif button32["text"] == "o" and button39["text"] == "o" and button46["text"] == "o" and button53["text"] == "o" and button60["text"] == "o":
        button32.config(bg="#80ffaa")
        button39.config(bg="#80ffaa")
        button46.config(bg="#80ffaa")
        button53.config(bg="#80ffaa")
        button60.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
# Hòa
def checkDraw():
    global count, win
    if count == 64 and win == False:
        messagebox.showinfo("OX Game", "DRAW!!")
        start()

def buttonClicked(button):
    global clicked, count
    if button["text"] == "" and clicked == True:
        button["text"] = "x"
        clicked = False
        count += 1
        checkWinner()
        checkDraw()
    elif button["text"] == "" and clicked == False:
        button["text"] = "o"
        clicked = True
        count += 1
        checkWinner()
        checkDraw()
    else:
        messagebox.showerror("OX Game", "LỖI!! Vui lòng chọn lại")

def start():
    global button1, button2, button3, button4, button5, button6, button7, button8
    global button9, button10, button11, button12, button13, button14, button15, button16
    global button17, button18, button19, button20, button21, button22, button23, button24
    global button25, button26, button27, button28, button29, button30, button31, button32
    global button33, button34, button35, button36, button37, button38, button39, button40
    global button41, button42, button43, button44, button45, button46, button47, button48
    global button49, button50, button51, button52, button53, button54, button55, button56
    global button57, button58, button59, button60, button61, button62, button63, button64
    global clicked, count, win
    
    clicked = True
    count = 0
    win = False
    
    # Xay dung cac nut cho tro choi
    button1 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button1))
    button2 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button2))
    button3 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button3))
    button4 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button4))
    button5 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button5))
    button6 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button6))
    button7 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button7))
    button8 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button8))
    
    button9 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button9))
    button10 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button10))
    button11 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button11))
    button12 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button12))
    button13 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button13))
    button14 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button14))
    button15 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button15))
    button16 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button16))
    
    button17 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button17))
    button18 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button18))
    button19 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button19))
    button20 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button20))
    button21 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button21))
    button22 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button22))
    button23 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button23))
    button24 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button24))
    
    button25 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button25))
    button26 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button26))
    button27 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button27))
    button28 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button28))
    button29 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button29))
    button30 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button30))
    button31 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button31))
    button32 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button32))
    
    button33 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button33))
    button34 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button34))
    button35 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button35))
    button36 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button36))
    button37 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button37))
    button38 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button38))
    button39 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button39))
    button40 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button40))
    
    button41 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button41))
    button42 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button42))
    button43 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button43))
    button44 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button44))
    button45 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button45))
    button46 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button46))
    button47 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button47))
    button48 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button48))
    
    button49 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button49))
    button50 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button50))
    button51 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button51))
    button52 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button52))
    button53 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button53))
    button54 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button54))
    button55 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button55))
    button56 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button56))
    
    button57 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button57))
    button58 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button58))
    button59 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button59))
    button60 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button60))
    button61 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button61))
    button62 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button62))
    button63 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button63))
    button64 = Button(root, text="", font=("Helvetica", 15), height=1, width=3, bg="SystemButtonFace", command=lambda: buttonClicked(button64))
    
    # Sap xep cac nut tren man hinh
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=0, column=3)
    button5.grid(row=0, column=4)
    button6.grid(row=0, column=5)
    button7.grid(row=0, column=6)
    button8.grid(row=0, column=7)
    
    button9.grid(row=1, column=0)
    button10.grid(row=1, column=1)
    button11.grid(row=1, column=2)
    button12.grid(row=1, column=3)
    button13.grid(row=1, column=4)
    button14.grid(row=1, column=5)
    button15.grid(row=1, column=6)
    button16.grid(row=1, column=7)
    
    button17.grid(row=2, column=0)
    button18.grid(row=2, column=1)
    button19.grid(row=2, column=2)
    button20.grid(row=2, column=3)
    button21.grid(row=2, column=4)
    button22.grid(row=2, column=5)
    button23.grid(row=2, column=6)
    button24.grid(row=2, column=7)
    
    button25.grid(row=3, column=0)
    button26.grid(row=3, column=1)
    button27.grid(row=3, column=2)
    button28.grid(row=3, column=3)
    button29.grid(row=3, column=4)
    button30.grid(row=3, column=5)
    button31.grid(row=3, column=6)
    button32.grid(row=3, column=7)
    
    button33.grid(row=4, column=0)
    button34.grid(row=4, column=1)
    button35.grid(row=4, column=2)
    button36.grid(row=4, column=3)
    button37.grid(row=4, column=4)
    button38.grid(row=4, column=5)
    button39.grid(row=4, column=6)
    button40.grid(row=4, column=7)
    
    button41.grid(row=5, column=0)
    button42.grid(row=5, column=1)
    button43.grid(row=5, column=2)
    button44.grid(row=5, column=3)
    button45.grid(row=5, column=4)
    button46.grid(row=5, column=5)
    button47.grid(row=5, column=6)
    button48.grid(row=5, column=7)
    
    button49.grid(row=6, column=0)
    button50.grid(row=6, column=1)
    button51.grid(row=6, column=2)
    button52.grid(row=6, column=3)
    button53.grid(row=6, column=4)
    button54.grid(row=6, column=5)
    button55.grid(row=6, column=6)
    button56.grid(row=6, column=7)
    
    button57.grid(row=7, column=0)
    button58.grid(row=7, column=1)
    button59.grid(row=7, column=2)
    button60.grid(row=7, column=3)
    button61.grid(row=7, column=4)
    button62.grid(row=7, column=5)
    button63.grid(row=7, column=6)
    button64.grid(row=7, column=7)
    
    # Tao menu tro choi
    gameMenu = Menu(root)
    root.config(menu=gameMenu)
    
    # Tao menu tuy chon
    optionMenu = Menu(gameMenu, tearoff=False)
    gameMenu.add_cascade(label="Options", menu=optionMenu)
    optionMenu.add_command(label="Restart Game", command=start)

start()
root.mainloop()