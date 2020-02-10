# Code that drawing oval

# calls for ezgraphics and imports it to GraphicsWindow
from ezgraphics import GraphicsWindow
win = GraphicsWindow()
canvas = win.canvas()

canvas.setOutline("red")     # Sets outline color to red
canvas.setFill("red")        # Color everything inside drawin (oval) to red
canvas.drawOval(150,150,100,100)    # Draws red oval

win.wait()
