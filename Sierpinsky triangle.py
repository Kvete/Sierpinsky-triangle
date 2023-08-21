from tkinter import Tk, Canvas, CENTER
from random import randint

polygon = [(200, 50), (50, 350), (350, 350)]
count = 0

root = Tk()
root.title("Sirpinsky triangle")
root.geometry("500x500")

canvas = Canvas(bg="white", width=400, height=400)
canvas.pack(anchor=CENTER, expand=1)
x = 50
y = 350
while count < 5000:
    temp = randint(0, len(polygon) - 1)
    if temp == 0:
        x = (x + polygon[0][0]) / 2
        y = (y + polygon[0][1]) / 2
    if temp == 1:
        x = (x + polygon[1][0]) / 2
        y = (y + polygon[1][1]) / 2
    if temp == 2:
        x = (x + polygon[2][0]) / 2
        y = (y + polygon[2][1]) / 2

    canvas.create_text(x, y, text="*", fill="#004D40")
    count += 1

root.mainloop()
