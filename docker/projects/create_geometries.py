from shapely.geometry import Point, LineString, Polygon

def createPointGeom(x1, y1, x2, y2, x3, y3, x4, y4):
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)
    p4 = Point(x4, y4)

    print("details and properties about point p1")
    print("type: ", type(p1))
    print("values: ", p1)
    print("cords: ", p1.xy)
    print("x: ", p1.x)
    print("y: ", p1.y)
    print("coords: ", p1.coords)


# def createLineGeom(x1, y1, x2, y2, x3, y3, x4, y4):
#     line1 = LineString([x1, y1])


def createPolyGeom():
    return


createPointGeom(0.0, 0.0, 2.2, 3.4, -4.5, 8.9, -7.4, -4.5)
# createLineGeom(0.0, 0.0, 2.2, 3.4, -4.5, 8.9, -7.4, -4.5)
