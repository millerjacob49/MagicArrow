from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Welcome to Magic Arrow!").grid(column=0, row=0)

def draw_arrow(canvas, x, y, direction):
    # Length and width of the arrow
    length = 50
    width = 10
    
    # Calculate the coordinates of the arrow points
    x0 = x
    y0 = y
    x1 = x + length * direction
    y1 = y
    x2 = x + length * 0.8 * direction
    y2 = y - width / 2
    x3 = x + length * 0.8 * direction
    y3 = y + width / 2
    
    # Draw the arrow on the canvas
    canvas.create_line(x0, y0, x1, y1, arrow=LAST, width=2)
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="black")

canvas = Canvas(frm, width=200, height=100) #this adds a "section" similar to div?
canvas.grid(column=0, row=1)

# Draw arrows on the canvas
draw_arrow(canvas, 100, 50, 1)  # Right arrow
draw_arrow(canvas, 100, 50, -1)  # Left arrow

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)    #adds a termination button(same as X)


root.mainloop() #puts everything on display, responds to user input until program terminates