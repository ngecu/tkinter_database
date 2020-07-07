from tkinter import *
import backend
from PIL import Image, ImageTk


def search_command():
    listing.delete(0,END)
    for row in backend.search(e1_value.get()):
        if row:
            listing.insert(END,row[1])
            label2.destroy()
            t1.delete('1.0', END)
            t1.config(fg='white')
            t1.insert(END,row[3])
            image = Image.open('static/{}.png'.format(e1_value.get()))
            
            image = image.resize((250,250), Image.ANTIALIAS)
            photo_image = ImageTk.PhotoImage(image)
            label = Label(f2, image = photo_image ,bg="#bfbfbf" )
            label.image = photo_image 
            label.place(relx=0.05,rely=0.1,relwidth=0.90,relheight=0.30)
        else:
            t1.delete('1.0', END)
            t1.config(fg='white')
            t1.insert(END,"No such word")
            
def result(event): 
    selection = listing.get(listing.curselection())

    for row in backend.search(selection):
        label2.destroy()
        listing.delete(0,END)
        t1.delete('1.0', END)
        listing.insert(END,row[1])
        t1.config(fg='white')
        t1.insert(END,row[3])
        image = Image.open('static/{}.png'.format(selection))
        
        image = image.resize((250,250), Image.ANTIALIAS)
        photo_image = ImageTk.PhotoImage(image)
        label = Label(f2, image = photo_image ,bg="#bfbfbf" )
        label.image = photo_image 
        label.place(relx=0.05,rely=0.1,relwidth=0.90,relheight=0.30)

  
def refresh_command():
    listing.delete(0,END)
    for row in backend.view():
        listing.insert(END,row[1])
    image = Image.open('static/logo.png')
    image = image.resize((250,250), Image.ANTIALIAS)
    photo_image = ImageTk.PhotoImage(image)
    label = Label(f2, image = photo_image ,bg="#bfbfbf" )
    label.image = photo_image 
    label.place(relx=0.05,rely=0.1,relwidth=0.90,relheight=0.30)
    t1.delete('1.0', END)

      


window = Tk()
window.title (" DevNgecu Dictionary")
window.geometry("1700x1000")


#ouput the definition of the word


outer_frame = Frame(window,bg="#bfbfbf")
outer_frame.place(relx=0,rely=0,relwidth=1,relheight=1)


#input of the word to search
e1_value=StringVar()
e1 = Entry(outer_frame,textvariable=e1_value,bg="#FFFD38",fg="black",justify = CENTER,font = ('courier', 30, 'bold'))
e1.place(relx=.35,rely=0,relwidth=0.60,relheight=.082)


b1 = Button(window,text="Search",command=search_command ,relief=FLAT,bg="green",fg="white",font = ('courier', 12, 'bold') )
b1.place(relx=0.85,rely=0,relwidth=0.1,relheight=.082)


b2 = Button(window,text="Refresh",command=refresh_command ,relief=FLAT,bg="red",fg="white",font = ('courier', 12, 'bold') )
b2.place(relx=0.025,rely=0.0,relwidth=0.25,relheight=.082)

f1 = Frame(outer_frame,bg="#bfbfbf")
f1.place(relx=0,rely=.082,relwidth=.3,relheight=.918)






f2 = Frame(outer_frame,bg="#bfbfbf")
f2.place(relx=0.3,rely=.082,relwidth=.7,relheight=.918)

listing = Listbox (f1,bg="white",relief=SUNKEN)
listing.place(relx=0.05,rely=0.05,relwidth=0.90,relheight=0.90)
listing.bind('<Double-Button>', result) 

t1 = Text(f2,relief=SUNKEN,bg="#444444",font = ('courier', 32, 'bold'))
t1.place(relx=0.05,rely=0.45,relwidth=0.90,relheight=0.50)




#seach button to execute command




listing.delete(0,END)
for row in backend.view():
    listing.insert(END,row[1])

image = Image.open('static/logo.png')
image = image.resize((250,250), Image.ANTIALIAS)
photo_image = ImageTk.PhotoImage(image)
label = Label(f2, image = photo_image ,bg="#bfbfbf" )
label.image = photo_image 
label.place(relx=0.05,rely=0.1,relwidth=0.90,relheight=0.30)


var = StringVar()
label2 = Label( f2, textvariable=var,bg="#bfbfbf" ,font = ('courier', 40, 'bold') )

# var.set("No of words are {}".format(len(backend.view())))
var.set("GUPTA DICTIONARY")
label2.place(relx=.2,rely=0.05,relwidth=0.5,relheight=.1,)




window.mainloop()