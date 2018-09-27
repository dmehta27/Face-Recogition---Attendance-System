import Tkinter as tk

def startgame():
    pass

mw = tk.Tk()              #Here I tried (1)
mw.title('The game')

back = tk.Frame(master=mw, width=500, height=500, bg='black')
back.pack()
