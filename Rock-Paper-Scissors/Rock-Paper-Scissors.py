from tkinter import *
import random

window = Tk()

color1 = "red"
color2 = "blue"
color3 = "green"
x = 0
y = 0
mouseup = True
play = False
win = 0
lose = 0

def buttondown(event):
    global mouseup
    mouseup = False

def buttonup(event):
    global mouseup
    mouseup = True


def where(event):
    global x
    global y
    print("moved to", event.x, event.y)
    x = event.x
    y = event.y

def animate():
    global mouseup
    global play
    global x
    global y
    if x >= 50 and x <= 100 and y >= 50 and y <= 100 and play == True and mouseup == False:
        game("Rock")
        mouseup = True
    elif x >= 150 and x <= 200 and y >= 50 and y <= 100 and play == True and mouseup == False:
        game("Paper")
        mouseup = True
    elif x >= 250 and x <= 300 and y >= 50 and y <= 100 and play == True and mouseup == False:
        game("Scissors")
        mouseup = True
    w.after(20, animate)

def key(event):
    global win
    global lose
    global y
    global x
    global play
    print("pressed", repr(event.char))
    letter = event.char
    if letter == "s":
        play = True
        SetColorS()
        message_label.configure(text="To end game, press 'e'")
        output_label.configure(text="Rock, Paper, Scissors! Game start!")
    elif letter == "e":
        play = False
        SetColorE()
        message_label.configure(text="To start game, press 's'")
        output_label.configure(text="Rock, Paper, Scissors!")
        win = 0
        lose = 0
        winscore_label.configure(text=str(win))
        losescore_label.configure(text=str(lose))

def exitbutton():
    window.destroy()

def SetColorS():
    w.itemconfigure(rock, image=gifRock)
    w.itemconfigure(paper, image=gifPaper)
    w.itemconfigure(scissors, image=gifScissors)
    #w.itemconfigure(rect1, fill="red", outline="red")
    #w.itemconfigure(rect2, fill="blue", outline="blue")
    #w.itemconfigure(rect3, fill="green", outline="green")

def SetColorE():
    w.itemconfigure(rock, image='')
    w.itemconfigure(paper, image='')
    w.itemconfigure(scissors, image='')
    #w.itemconfigure(rect1, fill="", outline="red")
    #w.itemconfigure(rect2, fill="", outline="blue")
    #w.itemconfigure(rect3, fill="", outline="green")

def reset():
    global win
    global lose
    win = 0
    lose = 0
    output_label.configure(text="Rock, Paper, Scissors! Score reseted!")
    winscore_label.configure(text=str(win))
    losescore_label.configure(text=str(lose))

def game(my_pick):
    global win
    global lose
    ai_pick = random.randint(1, 3)
    if ai_pick == 1:
        ai_pick = "Rock"
    elif ai_pick == 2:
        ai_pick = "Paper"
    elif ai_pick == 3:
        ai_pick = "Scissors"

    if my_pick == ai_pick:
        output_label.configure(text="Draw. Ai's pick is " + ai_pick)
    elif my_pick == "Rock" and ai_pick == "Paper":
        output_label.configure(text="You lose. Ai's pick is " + ai_pick)
        lose += 1
    elif my_pick == "Rock" and ai_pick == "Scissors":
        output_label.configure(text="You win. Ai's pick is " + ai_pick)
        win += 1
    elif my_pick == "Paper" and ai_pick == "Scissors":
        output_label.configure(text="You lose. Ai's pick is " + ai_pick)
        lose += 1
    elif my_pick == "Paper" and ai_pick == "Rock":
        output_label.configure(text="You win. Ai's pick is " + ai_pick)
        win += 1
    elif my_pick == "Scissors" and ai_pick == "Rock":
        output_label.configure(text="You lose. Ai's pick is " + ai_pick)
        lose += 1
    elif my_pick == "Scissors" and ai_pick == "Paper":
        output_label.configure(text="You win. Ai's pick is " + ai_pick)
        win += 1
    winscore_label.configure(text=str(win))
    losescore_label.configure(text=str(lose))


window.title("Rock, Paper, Scissors!")
w = Canvas(window, width=500, height=500)

message_label = Label(window, text="To start game, press 's'")
message_label.place(x=20, y=10)
output_label = Label(window, text="Rock, Paper, Scissors!")
output_label.place(x=180, y=10)

win_label = Label(window, text="win:")
win_label.place(x=20, y=140)
lose_label = Label(window, text="lose:")
lose_label.place(x=20, y=160)

winscore_label = Label(window, text="0")
winscore_label.place(x=50, y=140)
losescore_label = Label(window, text="0")
losescore_label.place(x=50, y=160)

rest_button = Button(window, text="Reset", command=reset)
rest_button.place(x=350, y=400)
exit_button = Button(window, text="Exit", command=exitbutton)
exit_button.place(x=400, y=400)

rect1 = w.create_rectangle(50, 50, 100, 100, outline="red")
rect2 = w.create_rectangle(150, 50, 200, 100, outline="blue")
rect3 = w.create_rectangle(250, 50, 300, 100, outline="green")

gifRock = PhotoImage(file='Rock.gif')
gifPaper = PhotoImage(file='Paper.gif')
gifScissors = PhotoImage(file='Scissors.gif')

rock = w.create_image(75, 75)
paper = w.create_image(175, 75)
scissors = w.create_image(275, 75)

w.focus_set()
w.bind("<ButtonPress-1>", buttondown)
w.bind("<ButtonRelease-1>", buttonup)
w.bind("<Key>", key)
w.bind("<Motion>", where)
w.pack()
animate()
window.mainloop()