from ezgraphics import *
import numpy as np

class Graphics:

    def __init__(self, row, col, box_width):

        self.margin = [5, 5, 5, 5]
        self.width = box_width*col + self.margin[1] + self.margin[3]
        self.height = box_width*row + self.margin[0] + self.margin[2]
        self.row = row
        self.col = col
        self.box_width = box_width
        self.win = GraphicsWindow(self.width, self.height)
        self.backgroundFill = [0, 0, 0]
        self.cellFill = [136, 8, 8]
        self.canvas = self.win.canvas()
        self.canvas.setBackground(*self.backgroundFill)
        self.win.setTitle("simulation")

    def draw(self, world):
        self.win.setTitle("simulation")
        self.canvas.clear()
        self.canvas.setOutline(*self.backgroundFill)
        for y, row in enumerate(world):
            for x, cell in enumerate(row):
                if cell:
                    self.canvas.setFill(*self.cellFill)
                    _ = [self.margin[3] + x*self.box_width, self.margin[0] + y*self.box_width]
                    self.canvas.drawRectangle(_[0], _[1], self.box_width, self.box_width)

    def wait(self):
        self.win.wait()



def World(dim):
    world = np.zeros((dim,dim))
    for i in range(dim):
        for j in range(dim):
            if i==j:
                world[i, j] = 1
    return world



ui = Graphics(50, 50, box_width=10)

ui.draw(World(50))
ui.wait()
