#Don't think main.py is necessary, but just for clarity
import Bluetooth
import graphing
import tkinter as tk
import time

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600

def main():
    # get data from bluetooth in 1 minute
    coordinate = []
    minute = 1
    t_end = (time.time() + 60) * minute
    while time.time() < t_end:
        coordinate.append(Bluetooth.getData())
        time.sleep(0.5) # sleep b/c don't want to get millions of data
    # draw on canvas
    window = tk.Tk()
    canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='grey')
    canvas.pack() # make width and height adjustment works on the canvas

    graphing.draw(coordinate, canvas)

main()