from tkinter import*
import random
screen=Tk()
screen.geometry("500x500")
screen.title("game")
screen.configure(bg="lightblue")
compscore=0
playscore=0
option=['rock',"paper","scissors"]
def game(uc):
    global(compscore,playscore)
    cc=random.choice(option)
    if uc==cc:
        title1.config(text="draw")
    elif uc=="rock" and cc=="paper":
        title1.config(text="computer wins")
        compscore+=1
    elif uc=="rock" and cc=="scissors":
        title1.config(text="player wins")
        playscore+=1
    elif uc=="paper" and cc=="rock":
        title1.config(text="player wins")
        playscore+=1
    elif uc=="paper" and cc=="scissors":
        title1.config(text="computer wins")
        compscore+=1
    elif uc=="scissors" and cc=="paper":
        title1.config(text="player wins")
        playscore+=1
    elif uc=="scissors" and cc=="rock":
        title1.config(text="computer wins")
        compscore+=1
rock=Label(screen, text="Rock Paper Scissors",bg="white",font=("arial",14))
rock.place(x=200, y=100)
title1=Label(screen, text="click to start",bg="white",font=("arial",14))
title1.place(x=250, y= 150)
rocky=Button(screen, text="Rock",bg="white",font=("arial",14))
rocky.place(x=100, y=200)
paper=Button(screen, text="Paper",bg="white",font=("arial",14))
paper.place(x=200, y=200)
scissors=Button(screen, text="Sissors",bg="white",font=("arial",14))
scissors.place(x=300, y=200)
sore=Label(screen, text="Score",bg="white",font=("arial",14))
sore.place(x=100, y=300)
score=Label(screen, text=" player Score",bg="white",font=("arial",14))
score.place(x=500, y=350)
core=Label(screen, text="computer Score",bg="white",font=("arial",14))
core.place(x=500, y=400)
playerselection=Label(screen, text="player selection:",bg="white",font=("arial",14))
playerselection.place(x=150, y=350)
computer=Label(screen, text="compute selection",bg="white",font=("arial",14))
computer.place(x=150, y=400)
screen.mainloop()
