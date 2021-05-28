def drawRectangle(t, w, h):
    drawSquare(t, w)

def drawSquare(tx, sz): # a new version of drawSquare
    drawRectangle(tx, sz, sz)

drawSquare(2, 3)
