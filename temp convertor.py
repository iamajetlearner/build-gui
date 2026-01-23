from tkinter import*
from tkinter import messagebox
screen=Tk()
screen.geometry("500x500")
screen.title("convertor")
screen.configure(bg="lightblue")
def show_info():
    c=userentry.get()
    f= (int(c)*9/5)+32
username=Label(screen, text="temp convertor c to f:",bg="lightblue",font=("arial",14))
username.place(x=50, y=100)
password=Label(screen, text="celcius:",bg="lightblue",font=("arial",14))
password.place(x=50, y=150)
userentry=Entry(screen)
userentry.place(x=150, y=100)
any=Label(screen, text="temp in farenheit:",bg="lightblue",font=("arial",14))
any.place(x=50, y=150)
submit=Button(bg="lightblue", text="convert",font=("arial",14), command=show_info)
submit.place(x=150,y=200)
screen.mainloop()
