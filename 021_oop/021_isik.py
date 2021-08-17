from tkinter import *
import tkinter as ttk
root = Tk()
root.title('ID Code checkers v0.1')
root.geometry('400x400')
root.resizable(width=False, height=False)
root.iconbitmap("favicon.ico")

id_entry_label = Label(root, text='Enter ID: ', bg='#FFFFFF')
id_entry_label.grid(row=0,column=1)
id_entry = Entry(root, width=35)
id_entry.grid(row=0, column=2)






root.mainloop()