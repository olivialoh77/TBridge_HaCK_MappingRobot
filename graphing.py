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
    car.x -= 10
    draw_path(canvas, car)

def move_right(event, canvas, car):
    car.x += 10
    draw_path(canvas, car)

def move_up(event, canvas, car):
    car.y -= 10
    draw_path(canvas, car)

def move_down(event, canvas, car):
    car.y += 10
    draw_path(canvas, car)

def draw_path(canvas, car):

    canvas.create_rectangle(car.x, car.y, car.x+car.size, car.y+car.size, fill='red')
    #canvas.move(car.rectangle,-1,0)
    #print('should redraw')
    #print(car.x)
    #canvas.update()

def draw_wall(event, canvas, car):
    length = 50
    delta = 100
    x = event.x
    y = event.y

    car_posX = car.x
    car_posY = car.y

    #canvas.create_line(x,y,x+length,y+length,fill='black')

    #vertical line
    if abs(car_posY-delta) <= abs(y) <= abs(car_posY+delta):
        canvas.create_line(x,y-length, x, y+length)

    #horizontal line
    elif abs(car_posX-delta) <= abs(x) <= abs(car_posX+delta):
        canvas.create_line(x-length, y, x+length, y)

    elif (x < car_posX and y < car_posY) or (x > car_posX and y > car_posY):
        canvas.create_line(x - length, y + length, x + length, y - length)

    elif (x < car_posX and y > car_posY) or (x > car_posX and y < car_posY):
        canvas.create_line(x - length, y - length, x + length, y + length)

    #diag topleft-bottomright
    #if abs(car_posX-delta) <= abs(x) <= abs(car_posX+delta)\
    #        and abs(car_posY-delta) <= abs(y) <= abs(car_posY+delta):
    '''if abs(car_posX-delta) <= abs(y) <= abs(car_posX+delta):
        canvas.create_line(x-length, y-length, x+length, y+length)
        print('topleft')
    
    #diag topright-bottomleft
    if abs(car_posY-delta) <= abs(x) <= abs(car_posY+delta)\
            and abs(car_posX-delta) <= abs(y) <=abs(car_posX+delta):
        canvas.create_line(x-length, y+length, x+length, y-length)
        print('topright')'''

def main():
    root = Tk()
    my_canvas = Canvas(root, width=window_width, height=window_height)
    my_canvas.pack()
    car = Car(my_canvas)
    root.bind("<KeyPress-Left>", lambda event: move_left(event, my_canvas, car))
    root.bind("<KeyPress-Right>", lambda event: move_right(event, my_canvas, car))
    root.bind("<KeyPress-Up>", lambda event: move_up(event, my_canvas, car))
    root.bind("<KeyPress-Down>", lambda event: move_down(event, my_canvas, car))
    root.bind("<Button-1>", lambda event: draw_wall(event, my_canvas, car))

    draw_path(my_canvas, car)
    mainloop()


main()