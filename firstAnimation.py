import tkinter as tk

root = tk.Tk()

WIDTH = 700
HEIGHT = 700

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()

x1 = WIDTH/2
y1 = HEIGHT/2

square1 = canvas.create_rectangle(x1,y1,x1-70,y1-70, fill="blue")
square2 = canvas.create_rectangle(x1,y1,x1+70,y1+70, fill="green")
square3 = canvas.create_rectangle(x1,y1,x1-70,y1+70, fill="black")
square4 = canvas.create_rectangle(x1,y1,x1+70,y1-70, fill="yellow")
def redraw():
    canvas.after(40,redraw)

    current_square1 = canvas.coords(square1)
    current_square2 = canvas.coords(square2)
    current_square3 = canvas.coords(square3)
    current_square4 = canvas.coords(square4)

    if current_square1[2] <= 0:
        canvas.move(square1, x1,y1)
    canvas.move(square1,-5,-5)
    
    if current_square2[0] >= WIDTH:
        canvas.move(square2, -x1,-y1)
    canvas.move(square2,+5,+5)
    
    if current_square3[2] <= 0:
        canvas.move(square3, x1,-y1)
    canvas.move(square3,-5,+5)
    
    if current_square4[0] >= WIDTH:
        canvas.move(square4, -x1,y1)
    canvas.move(square4,+5,-5) 
redraw()
root.mainloop()
