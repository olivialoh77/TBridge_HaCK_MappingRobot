import tkinter as tk

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500


coordinate = [(300, 300), (400, 300), (400, 500)]

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

    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill='red')

def drawObject(canvas, object_coordinate, car):
    #x = event.x
    #y = event.y
    print('wow')
    for (x,y) in object_coordinate:
        print(x)
        print(y)
        if car.x == x or car.y == x:
            print('true')
            canvas.create_oval(x-2, y-2, x+2, y+2, fill='blue')

def main():
    window = tk.Tk()
    my_canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='grey')
    my_canvas.pack()

    car = Car(my_canvas)

    window.bind("<KeyPress-Left>", lambda event: car.moveLeft(event, my_canvas))
    window.bind("<KeyPress-Right>", lambda event: car.moveRight(event, my_canvas))
    window.bind("<KeyPress-Up>", lambda event: car.moveUp(event, my_canvas))
    window.bind("<KeyPress-Down>", lambda event: car.moveDown(event, my_canvas))
    #window.bind("<Button-1>", lambda event: drawObject(event, my_canvas, coordinate, car))
    lambda event: drawObject(event, my_canvas, coordinate, car)
    window.mainloop()

main()