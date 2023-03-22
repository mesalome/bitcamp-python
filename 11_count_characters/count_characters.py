from tkinter import *

root = Tk()
var = StringVar()
push_number = StringVar()
var.set('hello')

def count(*args):
    value =  len(var.get())
    push_number.set(value)


start1 = Label(root, textvariable = var)
start1.pack()

start2 = Label(root, text = "has")
start2.pack()

l = Label(root, textvariable = push_number)
l.pack()

end = Label(root, text = "characters")
end.pack() 

t = Entry(root, textvariable = var)
t.pack()

t.bind('<KeyRelease>', count)


root.mainloop()