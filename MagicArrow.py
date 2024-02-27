from tkinter import *
from tkinter import ttk
import math

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Welcome to Magic Arrow!").grid(column=0, row=0)


def flip_arrow(canvas, orientation, color):
    pass

class Arrow:
    def __init__(self, canvas, orientation, color):
        self.orientation = orientation
        self.color = color
        self.draw_arrow(canvas, self.orientation, self.color)   #initialize & draw arrow
    
    def draw_arrow(self, canvas, orientation, color):
        # Length and width of the arrow
        length = 50
        width = 10
        x = 200
        y = 100
        
        # Convert orientation from degrees to radians
        angle_rad = math.radians(orientation)
        
        # Calculate the coordinates of the arrow points
        x0 = x
        y0 = y
        x1 = x + length * math.cos(angle_rad)
        y1 = y - length * math.sin(angle_rad)
        x2 = x + width / 2 * math.cos(angle_rad + math.pi / 2)
        y2 = y - width / 2 * math.sin(angle_rad + math.pi / 2)
        x3 = x - width / 2 * math.cos(angle_rad + math.pi / 2)
        y3 = y + width / 2 * math.sin(angle_rad + math.pi / 2)
        
        # Draw the arrow on the canvas
        canvas.create_line(x0, y0, x1, y1, arrow=LAST, width=5, fill=color)
        canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=color)

    def flip_arrow(self):
        pass        #TODO

class Trial:    
    
    def __init__(self, orientation, opacity):  #initialize a trial
        self.orientation = orientation
        self.opacity = opacity
        
        self.canvas = Canvas(frm, width=400, height=200, background='white') #this adds a "section" similar to div?
        self.canvas.grid(column=0, row=1)
        self.ans_arrow = None
        self.init_arrow = None
        

    def start(self):
        self.ans_arrow = Arrow(self.canvas, 235 + self.orientation, self.color(self.opacity))
        self.init_arrow = Arrow(self.canvas, 0 + self.orientation, 'black')

    def color(self, opacity):
        opacity = max(0, min(opacity, 100))
        value = int(255 - (opacity*2.55))
        hex_color = "#{:02X}{:02X}{:02X}".format(value, value, value)
        return hex_color
    
class Experiment:
    def __init__(self):
        pass


trial = Trial(0,15)  

ttk.Button(frm, text="Start Trial", command=trial.start).grid(column=2, row=1)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=1)    #adds a termination button(same as X)



root.mainloop() #puts everything on display, responds to user input until program terminates