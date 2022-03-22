# comma is  ,   (that's importan przecinek)

import tkinter as tk

#creaing window
window = tk.Tk()

#first txt in window
greeting = tk.Label(text="Hello, Tkinter", fg = "purple", bg = "white")
greeting.pack()

# color the text
kanapka = tk.Label(
    text="siemano, kolano",
    foreground = "red",
    background = "blue",
    width=20,
    height=10,
)
kanapka.pack()

#First button
button = tk.Button(
    text="kilkinj",
    foreground = "yellow",
    background = "green",
    width = 25,
    height = 5,
)
button.pack()

#first entry  (one line text)
entry = tk.Entry(fg = "red", bg = "white", width = 100)

entry.pack()

#first Text (lot of line txt)
text = tk.Text()
text.pack()

#First frame- idk what's doing
frame = tk.Frame()
frame.pack()

#event loop
window.mainloop()
