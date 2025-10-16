import tkinter
from tkinter import messagebox
import random

class MyApp:
    def __init__(self, parent):
        self.root = parent
        self.root.geometry("400x400")
        self.frame = tkinter.Frame(parent)
        self.frame.pack()

        self.random_delay = random.randint(3,6)*1000
        self.root.after(self.random_delay, self.delayed)

    def delayed(self):
        messagebox.showinfo('showinfo', '訊息測試')


if __name__ == "__main__":
    root = tkinter.Tk()
    app = MyApp(root)
    root.mainloop()