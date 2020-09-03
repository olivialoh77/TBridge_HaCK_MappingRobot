from tkinter import *

window_width = 500
window_height = 500

class Car():
    def __init__(self, master=None):
        #self.master = master
        self.canvas = Canvas(master)
        self.x = window_width / 2
        self.y = window_height - 100
        self.size = 20
        #self.rectangle = self.canvas.create_rectangle(self.x, self.y, self.x+self.size, self.y+self.size, fill='green')
        #self.canvas.pack()

    def get_pos(self):
        return (self.x, self.y)

    #def move_left(self, event):
    #    self.x -= 3
    #    draw_path(self.canvas, self)

def move_left(event, canvas, car):
    car.x -= 5
    draw_path(canvas, car)

def draw_path(canvas, car):

    canvas.create_rectangle(car.x, car.y, car.x+car.size, car.y+car.size, fill='red')
    #canvas.move(car.rectangle,-1,0)
    #print('should redraw')
    #print(car.x)
    #canvas.update()

def draw_wall(event, canvas, car):
    x = event.x
    y = event.y
    canvas.create_line(x,y,x+50,y+50,fill='black')


def main():
    root = Tk()
    my_canvas = Canvas(root, width=window_width, height=window_height)
    my_canvas.pack()
    car = Car(my_canvas)
    root.bind("<KeyPress-Left>", lambda event: move_left(event, my_canvas, car))
    root.bind("<Button-1>", lambda event: draw_wall(event, my_canvas, car))

    draw_path(my_canvas, car)
    mainloop()


main()