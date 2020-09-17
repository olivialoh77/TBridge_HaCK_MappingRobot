#Don't think main.py is necessary, but just for clarity
import Bluetooth
import graphing
import tkinter as tk
import time

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600

def main():

    # create canvas
    window = tk.Tk()
    canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='grey')
    canvas.pack() # make width and height adjustment works on the canvas

    # get data from bluetooth in 1 minute <- can change later
    coordinate = []
    minute = 1
    t_end = (time.time() + 60) * minute
    # send a list to drawing program
    while time.time() < t_end:
        coordinate.append(Bluetooth.getData())
        graphing.draw(coordinate, canvas)

    canvas.mainloop()

main()