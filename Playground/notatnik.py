import tkinter as tk
import sys

#Window of my notes
window = tk.Tk()

#Deffinition
def changebackground(event):
    color_red = tk.Button(bg="red")
    bg="red"
    color_red.pack()
    return color_red

#Choose the letters color
color_red = tk.Button(text = "Kolor czerwony",
                  fg="red",
                  bg="white",
                  width=200,
                  height=5)
color_red.pack()

color_red.bind("<Button-1>", changebackground)

color_black = tk.Button(text = "Kolor czarny",
                  fg="black",
                  bg="white",
                  width=200,
                  height=5)

color_black.pack()

color_orange = tk.Button(text = "Kolor pomarańczowy",
                  fg="orange",
                  bg="white",
                  width=200,
                  height=5)

color_orange.pack()

#Exit button
def quit(event):
    sys.exit()
exit_button = tk.Button(text="Click to exit the application",
                        width=200,
                        height=5)
exit_button.bind("<Button-1>", quit)
exit_button.pack()

#button.bind() z definicji!!!!!!!!!!!!

#Loop my notes (do not end it if i don't want)
window.mainloop()