import tkinter.colorchooser
from tkinter import *





root = Tk()
root.title('MyPy GUI 0.1')
root.geometry('800x600')
root.resizable(width=False, height=False)
# l1 = Label(root, text='MyPy Text Label')
#
# l2 = Label(text='MyPy Text Label V2', bg='black', fg='white').grid(row=2, column=2)
#
#
# l1.grid(row=0, column=0)

# colorchooser1 = tkinter.colorchooser.askcolor()
#
# number = 0
# def onClick():
#     if number != 10:
#         myLabel = Label(root, text='Hello World').grid()
#     else:
#         print('Done')


# button1 = Button(text='MyPy Button', fg='black', command=onClick).grid()
# def onclick():
#     myLabel = Label(root,text='Hello ' + in1.get())
#     myLabel.pack()
#
# in1 = Entry(root,width=100, bg='Black', fg='#25D500', borderwidth=10)
# in1.pack()
# in1.insert(0,'Please enter your name:')
#
# def onClick(event):
#     in1.delete(0, END)
#     in1.unbind('<Button-1>', onClickEntry)
#
# onClickEntry = in1.bind('<Button-1>', onClick)
#
# def onclick(number):
#     in1.delete(0,END)
#     in1.insert(0, int(number) ** 2)

#
# button1 = Button(text='MyPy Button', bg='Red', activebackground='Green', command=lambda:onclick(in1.get())).pack()



# root.iconbitmap("favicon.ico")
#
# MyPyImage = PhotoImage(file='py.png')
# MyPyImageLabel = Label(root, image=MyPyImage)
# MyPyImageLabel.pack()
#
# Button(root, text='End', command=root.quit).pack()

MyPyFrame = LabelFrame(root, text='SomeText', pady=50, padx=50).pack()
button = Button(MyPyFrame, text = 'Frame').pack()
#
root.mainloop()