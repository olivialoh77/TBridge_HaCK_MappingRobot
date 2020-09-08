import tkinter as tk
import csv

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600

car_queue = []
draw_flag = False
car_coordinate = []
object_coordinate = []

class Car():
    def __init__(self, canvas):
        self.x = 100
        self.y = 100
        self.size = 20
        #self.draw(canvas)
# for moving with keyboards and for debugging
'''
    def moveLeft(self, event, canvas):
        self.x -= 5
        self.draw(canvas)
        drawObject(canvas, car_coordinate, object_coordinate, self)

    def moveRight(self, event, canvas):
        self.x += 5
        self.draw(canvas)
        drawObject(canvas, car_coordinate, object_coordinate, self)

    def moveUp(self, event, canvas):
        self.y -= 5
        self.draw(canvas)
        drawObject(canvas, car_coordinate, object_coordinate, self)

    def moveDown(self, event, canvas):
        self.y += 5
        self.draw(canvas)
        drawObject(canvas, car_coordinate, object_coordinate, self)

    # Drawing a car onto canvas
    def draw(self, canvas):
        if(draw_flag):
            if len(car_queue) != 0:
                canvas.delete(car_queue[0])
                car_queue.pop()
                pass
        x = canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill='red')
        car_queue.append(x)

# Drawing object/wall/obstacles onto canvas
def drawObject(canvas, car_coordinate, object_coordinate, car):
    size = 3
    for (x,y) in object_coordinate:
        if car.x == x or car.y == x:
            canvas.create_oval(x-size, y-size, x+size, y+size, fill='blue')
'''
def main():
    
    # Create Tkinter window
    window = tk.Tk()
    my_canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='grey')
    my_canvas.pack() # make width and height adjustment works on the canvas

    car = Car(my_canvas)

    # Process csv file
    with open('data.txt') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        counter = 0
        for row in readCSV:
            if counter == 0:
                x_car = row[0].replace('(','')
                y_car = row[1].replace(')','')
                car_coordinate.append((x_car, y_car))
                counter += 1
            else:
                x_object = row[0].replace('(','')
                y_object = row[1].replace(')','')
                object_coordinate.append((x_object, y_object))
                counter -= 1

    # for resizing
    coeff = 30

    # draw car and object
    for car_coord in car_coordinate:

        my_canvas.create_rectangle(float(car_coord[0]) * coeff, float(car_coord[1]) * coeff, 
        float(car_coord[0]) * coeff + car.size, float(car_coord[1]) * coeff + car.size, fill='green')

    for obj_coord in object_coordinate:
        my_canvas.create_oval(float(obj_coord[0]) * coeff, float(obj_coord[1]) * coeff, 
        float(obj_coord[0]) * coeff + 5, float(obj_coord[1]) * coeff + 5, fill='blue')
    '''        
    # Key bindings for testing
    window.bind("<KeyPress-Left>", lambda event: car.moveLeft(event, my_canvas))
    window.bind("<KeyPress-Right>", lambda event: car.moveRight(event, my_canvas))
    window.bind("<KeyPress-Up>", lambda event: car.moveUp(event, my_canvas))
    window.bind("<KeyPress-Down>", lambda event: car.moveDown(event, my_canvas))
    #window.bind("<Button-1>", lambda event: drawObject(event, my_canvas, coordinate, car))
    '''
    
    window.mainloop() # keep looping until there's a new event

main()