import matplotlib.pyplot as plt
import matplotlib.patches as patches
import itertools


class BoardView:
    n = 20
    my_dpi = 20
    canvasSize = (n,n)

    def __init__(self):
        self.rects = {}
        self.fig, self.ax = self.createCanvas(self.canvasSize)
    
        color = "#DCDCDC"
        for row, col in itertools.product(range(self.n), range(self.n)):
            rect = self.createRectangle((1,1),(col,row),self.canvasSize,color)
            self.rects[(row, col)] = rect
            self.ax.add_patch(rect)

    def createCanvas(self, shape):
        fig,ax = plt.subplots(1)
        fig.dpi= self.my_dpi
        fig.set_size_inches(*shape)
        ax.set_xticks([])
        ax.set_yticks([])
        return fig, ax

    def set_point_color(point, val):
        color = self.get_color(val)
        self.rects[(point.x, point.y)].setColor(color)

    def display(self):
        self.fig.show()

    def createRectangle(self, wh, xy, cwch, color="black"):
        """
        All units are in inches. 

        Parameters
        ==========
        wh: (width,height) 
        xy: (x,y)
        cwch: (canvasWidth,canvasHeight)
        """
        return patches.Rectangle((xy[0]/cwch[0],xy[1]/cwch[1]),wh[0]/cwch[0],wh[1]/cwch[1],color=color)

    def get_color(self, val):
        mapping = {
            -1: "#DCDCDC",
            0: "yellow",
            1: "red",
            2: "green",
            3: "blue",
            4: "orange",
            5: "purple",
            6: "black"
        }
        return mapping[val]
