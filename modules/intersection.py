# module for intersection points for lines from file
import matplotlib.pyplot as plt 
from modules.drawGraph import draw
import datetime

def getLines(file):
    tmp = sorted([l.split('\n')[0] for l in file if len(l.split(' ')) == 3])
    if (len(tmp) > 0) :
        lines = [tmp[0]]
        for i in range(1, len(tmp)) :
            if (not (tmp[i] == tmp[i - 1])) : 
                lines.append(tmp[i])

        toFloat = lambda t : (float(t[0]), float(t[1]), float(t[2]))
        parseString = lambda line: (line.split(' '))
        return [toFloat(parseString(l)) for l in lines]
    return []


def isParallelLines(l1, l2):
    # A1B2 - A2B1 = 0
    return (l1[0] * l2[1] - l2[0] * l1[1]) == 0

def intersectionPoint(l1, l2):
    det = l1[0] * l2[1] - l2[0] * l1[1]             # A1B2 - A2B1
    x = (l1[1] * l2[2] - l2[1] * l1[2]) / det       # (B1C2 - B2C1) / det
    y = (l2[0] * l1[2] - l1[0] * l2[2]) / det       # (A2C1 - A1C2) / det
    return (x, y)

def IntersectionLines(file):
    lines = getLines(file)
    n = len(lines)
    i = 0
    counter = 0
    t1 = datetime.datetime.now()
    while (i < n) :
        j = i + 1
        while (j < n) :
            if (not isParallelLines(lines[i], lines[j])) :
                counter = counter + 1
            j = j + 1
        i = i + 1
    t2 = datetime.datetime.now()

    for line in lines :
        print("Line: %dx + %dy + %d = 0"% line)
    print("\nCount intersection points: ", counter)
    print("Time: ", t2 - t1)

def IntersectionLinesWithDraw(file):
    lines = getLines(file)
    n = len(lines)
    i = 0
    counter = 0
    points = []
    while (i < n) :
        j = i + 1
        while (j < n) :
            if (not isParallelLines(lines[i], lines[j])) :
                counter = counter + 1
                points.append(intersectionPoint(lines[i], lines[j]))   # only for draw
            j = j + 1
        i = i + 1

    for line in lines :
        print("Line: %dx + %dy + %d = 0"% line)
    print("\nCount intersection points: ", counter)

    draw(lines, points)        