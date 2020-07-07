from tkinter import *
import papa

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])


def view_command():
    list1.delete(0,END)
    for row in papa.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in papa.search(word_text.get(),link_text.get(),definition_text.get()):
        list1.insert(END,row)

def add_command():
    papa.insert(word_text.get(),link_text.get(),definition_text.get())
    list1.delete(0,END)
    list1.insert(END,(word_text.get(),link_text.get(),definition_text.get()))

def delete_command():
    papa.delete(selected_tuple[0])

def update_command():
    papa.update(selected_tuple[0],word_text.get(),link_text.get(),definition_text.get())

window=Tk()

window.wm_title("Settings")

l1=Label(window,text="Word")
l1.grid(row=0,column=0)

l2=Label(window,text="Link")
l2.grid(row=0,column=2)

l3=Label(window,text="Definition")
l3.grid(row=1,column=0)


word_text=StringVar()
e1=Entry(window,textvariable=word_text)
e1.grid(row=0,column=1)

link_text=StringVar()
e2=Entry(window,textvariable=link_text)
e2.grid(row=0,column=3)

definition_text=StringVar()
e3=Entry(window,textvariable=definition_text)
e3.grid(row=1,column=1)



list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=12,command=view_command)
b1.grid(row=2,column=3)


b3=Button(window,text="Add entry", width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected", width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
