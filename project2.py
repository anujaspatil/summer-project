from tkinter import *

from PIL import ImageTk,Image

root=Tk()

canvas=Canvas(root, width=3000, height=500)
image=ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Documents\\GitHub\\summer-project\\robot.png"))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

root.mainloop()