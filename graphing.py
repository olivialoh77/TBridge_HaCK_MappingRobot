import tkinter as tk

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

rect_queue = []
draw_flag = False

coordinate = [(150, 300), (300, 300), (200, 50),\
    (50, 400)]

class Car():
    def __init__(self, canvas):
        self.x = 100
        self.y = 100
        self.size = 20
        self.draw(canvas)
    
    def moveLeft(self, event, canvas):
        self.x -= 5
        self.draw(canvas)
        drawObject(canvas, coordinate, self)

    def moveRight(self, event, canvas):
        self.x += 5
        self.draw(canvas)
        drawObject(canvas, coordinate, self)

    def moveUp(self, event, canvas):
        self.y -= 5
        self.draw(canvas)
        drawObject(canvas, coordinate, self)

    def moveDown(self, event, canvas):
        self.y += 5
        self.draw(canvas)
        drawObject(canvas, coordinate, self)

    # Drawing a car onto canvas
    def draw(self, canvas):
        if(draw_flag):
            if len(rect_queue) != 0:
                canvas.delete(rect_queue[0])
                rect_queue.pop()
                pass
        x = canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill='red')
        rect_queue.append(x)

# Drawing object/wall/obstacles onto canvas
def drawObject(canvas, object_coordinate, car):
    size = 3
    for (x,y) in object_coordinate:
        if car.x == x or car.y == x:
            canvas.create_oval(x-size, y-size, x+size, y+size, fill='blue')

def main():

    # Create Tkinter window
    window = tk.Tk()
    my_canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='grey')
    my_canvas.pack()

    car = Car(my_canvas)

    # Key bindings for testing
    window.bind("<KeyPress-Left>", lambda event: car.moveLeft(event, my_canvas))
    window.bind("<KeyPress-Right>", lambda event: car.moveRight(event, my_canvas))
    window.bind("<KeyPress-Up>", lambda event: car.moveUp(event, my_canvas))
    window.bind("<KeyPress-Down>", lambda event: car.moveDown(event, my_canvas))
    #window.bind("<Button-1>", lambda event: drawObject(event, my_canvas, coordinate, car))
    window.mainloop() # keep looping until there's a new event

main()