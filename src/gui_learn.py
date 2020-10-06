from tkinter import *


def Button_():
    r = Tk()
    r.title('Counting Seconds')
    button = Button(r, text='Stop', width=25, command=r.destroy)
    button.pack()
    r.mainloop()

# Button_()


def Canvas_():
    master = Tk()
    w = Canvas(master, width=40, height=60)
    w.pack()
    canvas_height = 20
    canvas_width = 200
    y = int(canvas_height / 2)
    w.create_line(0, y, canvas_width, y)
    master.mainloop()

# Canvas_()


def a():
    global var2
    print(var2.get())


# master = Tk()
# var2 = IntVar()


def CheckButton_():
    global var2, master

    var1 = IntVar()
    Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)

    Checkbutton(master, text='female', variable=var2,
                command=a).grid(row=1, sticky=W)
    mainloop()


# CheckButton_()


def Entry_():
    master = Tk()
    master.minsize(300, 100)
    Label(master, text='First Name').grid(row=0)
    Label(master, text='Last Name').grid(row=1)
    e1 = Entry(master)
    e2 = Entry(master)
    e1.grid(row=0, column=1, sticky=W)
    for i in range(7):
        master.grid_columnconfigure(i, weight=1, uniform="foo")
    # e2.grid(row=1, column=1, columnspan=5)
    # master.grid_columnconfigure(0, weight=3, uniform="foo")
    e2.grid(row=1, column=1, columnspan=5, sticky="nsew")
    mainloop()


# Entry_()


def Frame_():
    root = Tk()
    frame = Frame(root)
    root.minsize(300, 100)
    frame.pack()
    bottomframe = Frame(root)
    bottomframe.pack(side=BOTTOM)
    redbutton = Button(frame, text='Red', fg='red')
    redbutton.pack(side=LEFT)
    greenbutton = Button(frame, text='Brown', fg='brown')
    greenbutton.pack(side=LEFT)
    bluebutton = Button(frame, text='Blue', fg='blue')
    bluebutton.pack(side=LEFT)
    blackbutton = Button(bottomframe, text='Black', fg='black')
    blackbutton.pack(side=BOTTOM)
    root.mainloop()


# Frame_()


def Listbox_():
    top = Tk()
    Lb = Listbox(top)
    Lb.grid(row=0, column=0, sticky="wens")
    top.grid_columnconfigure(0, weight=1, uniform="foo")
    # Lb.config(width=0, height=0)
    Lb.insert(1, 'Python')
    Lb.insert(2, 'Java')
    Lb.insert(3, 'C++')
    Lb.insert(4, 'Any other')
    # Lb.pack()
    top.mainloop()


# Listbox_()


def MenuButton_():
    top = Tk()
    mb = Menubutton(top, text="GfG")
    mb.grid()
    mb.menu = Menu(mb, tearoff=0)
    mb["menu"] = mb.menu
    cVar = IntVar()
    aVar = IntVar()
    mb.menu.add_checkbutton(label='Contact', variable=cVar)
    mb.menu.add_checkbutton(label='About', variable=aVar)
    mb.pack()
    top.mainloop()


# MenuButton_()


def Menu_():
    root = Tk()
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New')
    filemenu.add_command(label='Open...')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=root.quit)
    helpmenu = Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About')
    mainloop()


# Menu_()

def Message_():
    main = Tk()
    ourMessage = 'This is our Message'
    messageVar = Message(main, text=ourMessage)
    messageVar.config(bg='lightgreen')
    messageVar.pack()
    main.mainloop()


Message_()
