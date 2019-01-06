import matplotlib.pyplot as plt
import matplotlib.patches as patches

class GameView:

    def __init__(self):
        pass
    
    def display(self, game):
        n = 20
        my_dpi = 20
        canvasSize = (n,n)
        fig,ax = self.createCanvas(canvasSize[0],canvasSize[1],my_dpi)
        color = "black"

        for row in range(n):
            for col in range(n):
                color = self.get_color(game, (20 * row + col))
                rect = self.createRectangle((1,1),(col,row),canvasSize,color)
                ax.add_patch(rect)

        plt.show()

    def createCanvas(self, width,height,my_dpi):
        fig,ax = plt.subplots(1)
        fig.dpi= my_dpi
        fig.set_size_inches(width,height)
        ax.set_xticks([])
        ax.set_yticks([])
        return fig,ax

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

    def get_color(self, game, index):
 
              
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

        mask = 1 << (index)

        for i, player in enumerate(game.players):

            if player.full & mask:
                return mapping[i]

        return mapping[-1]
            
