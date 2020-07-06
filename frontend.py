from tkinter import *
import backend


def view_command():
    
window = Tk()
window.title (" DevNgecu Dictionary")
window.geometry("600x400")


#ouput the definition of the word


outer_frame = Frame(window,bg="#bfbfbf")
outer_frame.place(relx=0,rely=0,relwidth=1,relheight=1)


#input of the word to search
e1_value=StringVar()
e1 = Entry(outer_frame,textvariable=e1_value,bg="#FFFD38",fg="black",justify = CENTER,font = ('courier', 30, 'bold'))
e1.place(relx=0,rely=0,relwidth=1.0,relheight=.082)

f1 = Frame(outer_frame,bg="#bfbfbf")
f1.place(relx=0,rely=.082,relwidth=.3,relheight=.918)





f2 = Frame(outer_frame,bg="#bfbfbf")
f2.place(relx=0.3,rely=.082,relwidth=.7,relheight=.918)

listing = Listbox (f1,bg="white",relief=SUNKEN)
listing.place(relx=0.05,rely=0.05,relwidth=0.90,relheight=0.90)

t1 = Text(f2,fg="white",relief=SUNKEN,bg="#444444",font = ('courier', 20, 'bold'))
t1.place(relx=0.05,rely=0.05,relwidth=0.90,relheight=0.50)

t2 = Text(f2,fg="black",relief=SUNKEN,bg="white",font = ('courier', 20, 'bold'))
t2.place(relx=0.05,rely=0.55,relwidth=0.90,relheight=0.39)


#seach button to execute command

b1 = Button(t1,text="Search",command=view_command ,relief=FLAT,bg="green",fg="white",font = ('courier', 30, 'bold') )
b1.place(relx=0,rely=0,relwidth=1,relheight=.52)



window.mainloop()