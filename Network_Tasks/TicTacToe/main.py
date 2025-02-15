# Tic-Tac-Toe:
from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Welcome to The Game ")
window.geometry("400x300")

lbl = Label(window, text="Tic-tac-toe Game", font=('Helvetica', '15'))
lbl.grid(row=0, column=0)
lbl = Label(window, text="Player 1: X", font=('Helvetica', '10'))
lbl.grid(row=1, column=0)
lbl = Label(window, text="Player 2: O", font=('Helvetica', '10'))
lbl.grid(row=2, column=0)

turn = 1


def Reset():
    global flag, turn
    flag = 1
    turn = 1
    btn1["text"] = " "
    btn2["text"] = " "
    btn3["text"] = " "
    btn4["text"] = " "
    btn5["text"] = " "
    btn6["text"] = " "
    btn7["text"] = " "
    btn8["text"] = " "
    btn9["text"] = " "


def Clicked1():
    global turn
    if btn1["text"] == " ":
        if turn == 1:
            turn = 2
            btn1["text"] = "X"
        elif turn == 2:
            turn = 1
            btn1["text"] = "O"
        Check()


def Clicked2():
    global turn
    if btn2["text"] == " ":
        if turn == 1:
            turn = 2
            btn2["text"] = "X"
        elif turn == 2:
            turn = 1
            btn2["text"] = "O"
        Check()


def Clicked3():
    global turn
    if btn3["text"] == " ":
        if turn == 1:
            turn = 2
            btn3["text"] = "X"
        elif turn == 2:
            turn = 1
            btn3["text"] = "O"
        Check()


def Clicked4():
    global turn
    if btn4["text"] == " ":
        if turn == 1:
            turn = 2
            btn4["text"] = "X"
        elif turn == 2:
            turn = 1
            btn4["text"] = "O"
        Check()


def Clicked5():
    global turn
    if btn5["text"] == " ":
        if turn == 1:
            turn = 2
            btn5["text"] = "X"
        elif turn == 2:
            turn = 1
            btn5["text"] = "O"
        Check()


def Clicked6():
    global turn
    if btn6["text"] == " ":
        if turn == 1:
            turn = 2
            btn6["text"] = "X"
        elif turn == 2:
            turn = 1
            btn6["text"] = "O"
        Check()


def Clicked7():
    global turn
    if btn7["text"] == " ":
        if turn == 1:
            turn = 2
            btn7["text"] = "X"
        elif turn == 2:
            turn = 1
            btn7["text"] = "O"
        Check()


def Clicked8():
    global turn
    if btn8["text"] == " ":
        if turn == 1:
            turn = 2
            btn8["text"] = "X"
        elif turn == 2:
            turn = 1
            btn8["text"] = "O"
        Check()


def Clicked9():
    global turn
    if btn9["text"] == " ":
        if turn == 1:
            turn = 2
            btn9["text"] = "X"
        elif turn == 2:
            turn = 1
            btn9["text"] = "O"
        Check()

flag = 1

def Check():
    global flag
    b1 = btn1["text"]
    b2 = btn2["text"]
    b3 = btn3["text"]
    b4 = btn4["text"]
    b5 = btn5["text"]
    b6 = btn6["text"]
    b7 = btn7["text"]
    b8 = btn8["text"]
    b9 = btn9["text"]
    flag = flag + 1
    if b1 == b2 and b1 == b3 and b1 == "O" or b1 == b2 and b1 == b3 and b1 == "X":
        win(btn1["text"])
    if b4 == b5 and b4 == b6 and b4 == "O" or b4 == b5 and b4 == b6 and b4 == "X":
        win(btn4["text"])
    if b7 == b8 and b7 == b9 and b7 == "O" or b7 == b8 and b7 == b9 and b7 == "X":
        win(btn7["text"])
    if b1 == b4 and b1 == b7 and b1 == "O" or b1 == b4 and b1 == b7 and b1 == "X":
        win(btn1["text"])
    if b2 == b5 and b2 == b8 and b2 == "O" or b2 == b5 and b2 == b8 and b2 == "X":
        win(btn2["text"])
    if b3 == b6 and b3 == b9 and b3 == "O" or b3 == b6 and b3 == b9 and b3 == "X":
        win(btn3["text"])
    if b1 == b5 and b1 == b9 and b1 == "O" or b1 == b5 and b1 == b9 and b1 == "X":
        win(btn1["text"])
    if b7 == b5 and b7 == b3 and b7 == "O" or b7 == b5 and b7 == b3 and b7 == "X":
        win(btn7["text"])
    if flag == 10:
        messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
        window.destroy()


def win(player):
    result = "Game Complete " + player + " wins "
    messagebox.showinfo("Congratulations", result)
    window.destroy()


btn1 = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=Clicked1)
btn1.grid(column=1, row=1)
btn2 = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=Clicked2)
btn2.grid(column=2, row=1)
btn3 = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=Clicked3)
btn3.grid(column=3, row=1)
btn4 = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=Clicked4)
btn4.grid(column=1, row=2)
btn5 = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=Clicked5)
btn5.grid(column=2, row=2)
btn6 = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=Clicked6)
btn6.grid(column=3, row=2)
btn7 = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=Clicked7)
btn7.grid(column=1, row=3)
btn8 = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=Clicked8)
btn8.grid(column=2, row=3)
btn9 = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=Clicked9)
btn9.grid(column=3, row=3)

reset_btn = Button(window, text="Reset", bg="white", fg="Black", width=5, height=1, font=('Helvetica', '12'), command=Reset)
reset_btn.grid(column=2, row=4)

window.mainloop()
