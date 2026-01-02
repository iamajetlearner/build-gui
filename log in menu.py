from tkinter import*
from tkinter import messagebox
screen=Tk()
screen.geometry("500x500")
screen.title("login menu")
screen.configure(bg="lightblue")
def show_info():
    messagebox.showinfo("information","hello hehehehehehee")
username=Label(screen, text="username:",bg="lightblue",font=("arial",14))
username.place(x=50, y=100)
password=Label(screen, text="password:",bg="lightblue",font=("arial",14))
password.place(x=50, y=150)
userentry=Entry(screen)
userentry.place(x=150, y=100)
passwordentry=Entry(screen)
passwordentry.place(x=150,y=150)
submit=Button(bg="lightblue", text="submit",font=("arial",14), command=show_info)
submit.place(x=150,y=200)
screen.mainloop()
