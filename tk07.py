import tkinter as tk

def print_txtval():
    val_en = en.get()
    print(val_en)
root = tk.Tk()
root.title('Widget+Action')
root.geometry('350x150')
lb = tk.Label(text='Label-1')
en = tk.Entry()
bt = tk.Button(text='Button-1', command=print_txtval)
[widget.pack() for widget in [lb,bt,en]]
 #or
#lb.pack()
#en.pack()
#bt.pack()
root.mainloop()