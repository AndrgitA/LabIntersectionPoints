import matplotlib.pyplot as plt

def drawLine(line, x1, x2, y1, y2, h) :
    (a, b, c) = line
    X = Y = []
    countX = int(abs((x2 - x1) / h))
    countY = int(abs((y2 - y1) / h))
    if (a == 0.0 or b == 0.0) :
        if (a == 0.0) :               # by + c = 0
            X = [x1 + i * h for i in range(0, countX)]
            Y = [(-c) / b] * countX
        else :                      # ax + c = 0
            X = [(-c) / a] * countY
            Y = [y1 + i * h for i in range(0, countY)]
    else :                          # ax + by + c = 0
        X = [x1 + i * h for i in range(0, countX)]
        Y = [(-(a * i + c)) / b for i in X]
    name = "line {}x + {}y + {} = 0".format(a, b, c)
    plt.plot(X, Y, label = name ) 

def drawPoint(point) :
    plt.scatter(point[0], point[1], s=20, color=[ "#A70F00"])
    pass

def draw(lines, points):
    h = 0.1                         #step
    x1 = x2 = y1 = y2 = 0
    nPoints = len(points)
    if (nPoints > 0) :              #get [x1, x2] & [y1, y2] rect
        x1 = x2 = points[0][0]
        y1 = y1 = points[0][1]
        i = 1
        while (i < nPoints) :
            if (points[i][0] < x1) : x1 = points[i][0]
            elif (points[i][0] > x2) : x2 = points[i][0]

            if (points[i][1] < y1) : y1 = points[i][1]
            elif (points[i][1] > y2) : y2 = points[i][1]
            i = i + 1
        x1 = x1 - 10
        x2 = x2 + 10
        y1 = y1 - 10
        y2 = y2 + 10
    else :
        x1 = y1 = -20
        x2 = y2 = 20

    # draw lines
    for line in lines :
        if (line[0] != 0.0 or line[1] != 0.0) :
            drawLine(line, x1, x2, y1, y2, h)
    

    # draw points
    for point in points :
        drawPoint(point)

    plt.xlabel('x - axis') 
    plt.ylabel('y - axis') 
    plt.title('Intersection points') 
    plt.legend()
    plt.show() 
