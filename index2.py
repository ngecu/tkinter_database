import tkinter as tk


#configure window settings
win = tk.Tk()
win.configure(background = "green")
win.title("ECO-DICTIONARY")
#first word(button)
def clicked():
    word_1d = tk.Label(win, text="word_1d",bg="red",font = ("Arial Bold",21),relief="raised")
    word_1d.pack(side="top",anchor="n")

word_1 = tk.Button(win, text = "word_1", bg = "light blue",font = ("Arial Bold",15), relief="groove",command=clicked)
word_1.pack(side="top",anchor="nw")
win.geometry('750x500')

#search bar
search = tk.Entry(win,text="search bar",bg="white",font=("Arial Bold",15)).pack(side="bottom",fill="x")

win.mainloop()