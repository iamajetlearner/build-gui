from tkinter import*
import calendar
from tkinter import messagebox
screen=Tk()
screen.geometry("500x500")
screen.title("calendar")
screen.configure(bg="lightblue")
def show_info():
    new_gui = Tk()
    new_gui.geometry("550x600")
    fetch_year= int(year_entry.get())
    cal_content= calendar.calendar(fetch_year)
    cal_year= Label(new_gui,text=cal_content,justify="right",font="consolas 8 bold")
    cal_year.place(x=50,y=100)
title=Label(screen, text="calendar",bg="lightblue",font=("arial",14))
title.place(x=50, y=50)
title2=Label(screen, text="enter the year",bg="lightblue",font=("arial",14))
title2.place(x=50, y=100)
year_entry=Entry(screen)
year_entry.place(x=200, y=135)
submit=Button(bg="lightblue", text="submit",font=("arial",14), command=show_info)
submit.place(x=150,y=150)
screen.mainloop()
