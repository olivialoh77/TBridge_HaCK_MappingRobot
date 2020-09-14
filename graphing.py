import tkinter as tk
import csv

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600

car_queue = []
car_coordinate = []
object_coordinate = []

data_string = "14,1,10,4"
data_string_2 = [15,2,11,5]

def draw(data_string, canvas):
    # Create Tkinter window
    '''window = tk.Tk()
    my_canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='grey')
    my_canvas.pack() # make width and height adjustment works on the canvas
'''
    if isinstance(data_string, str):
        readCSV = csv.reader([data_string], delimiter=',')
        counter = 0
        for row in readCSV:
            x_car = row[0]
            y_car = row[1]
            x_object = row[2]
            y_object = row[3]
    else:
        for row in data_string:
            x_car = row[0]
            y_car = row[1]
            x_object = row[2]
            y_object = row[3]

    car_coordinate.append((x_car, y_car))
    object_coordinate.append((x_object, y_object))
    #print(car_coordinate)
    #print(object_coordinate)

    # for resizing
    coeff = 30
    size = 20

    # draw car and object
    for car_coord in car_coordinate:

        canvas.create_rectangle(float(car_coord[0]) * coeff, float(car_coord[1]) * coeff, 
        float(car_coord[0]) * coeff + size, float(car_coord[1]) * coeff + size, fill='green')

    for obj_coord in object_coordinate:
        canvas.create_oval(float(obj_coord[0]) * coeff, float(obj_coord[1]) * coeff, 
        float(obj_coord[0]) * coeff + 5, float(obj_coord[1]) * coeff + 5, fill='blue')
    
    canvas.mainloop() # keep looping until there's a new event

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
            
    # Key bindings for testing
    window.bind("<KeyPress-Left>", lambda event: car.moveLeft(event, my_canvas))
    window.bind("<KeyPress-Right>", lambda event: car.moveRight(event, my_canvas))
    window.bind("<KeyPress-Up>", lambda event: car.moveUp(event, my_canvas))
    window.bind("<KeyPress-Down>", lambda event: car.moveDown(event, my_canvas))
    #window.bind("<Button-1>", lambda event: drawObject(event, my_canvas, coordinate, car))
    
    
    window.mainloop() # keep looping until there's a new event

main()
'''
#FOR TESTING
#draw(data_string)
#draw(data_string_2)