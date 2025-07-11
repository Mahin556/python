import tkinter as tk
from time import strftime #to format a time

root = tk.Tk() #root window/object
root.title("Digital Clock")

def time():
    string=strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,time)

label = tk.Label(root, font=('calibri', 50, 'bold'), background='black', foreground='green')
label.pack(anchor='center')

time()

root.mainloop()

