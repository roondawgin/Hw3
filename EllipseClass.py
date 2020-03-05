import utility


class Ellipse:

    def __init__(self, x1=0, y1=0, x2=1, y2=0, semiMajor=1):

        self.x1 = x1
        if type(self.x1) == str:
            raise TypeError('Numbers Only Please')

        self.y1 = y1
        if type(self.y1) == str:
            raise TypeError('Numbers Only Please')

        self.x2 = x2
        if type(self.x2) == str:
            raise TypeError('Numbers Only Please')

        self.y2 = y2
        if type(self.y2) == str:
            raise TypeError('Numbers Only Please')

        self.semiMajor = semiMajor
        if self.x1 == self.x2 or self.y1 == self.y2:
            if self.semiMajor <= utility.distance((self.x1, self.y1), (self.x2, self.y2))/2:
                raise ValueError('semiMajor must be larger than half the distance between Foci1 and Foci2')
        else:
            raise ValueError('X1 and X2 or Y1 and Y2 must be equal')

    def setFoci1(self, x1, y1):
        """setting foci 1 of ellipse"""
        self.F1 = (self.x1, self.y1)

    def setFoci2(self, x2, y2):
        """setting foci 2 of ellipse"""
        self.F1 = (self.x2, self.y2)

    def setsemiMajor(self, semiMajor):
        """setting Semi Major of ellipse"""
        self.semiMajor = semiMajor

    def getFoci1(self):
        """Returns foci 1 of ellipse"""
        return (self.x1, self.y1)

    def getFoci2(self, ):
        """Returns foci 2 of ellipse"""
        return (self.x2, self.y2)

    def getsemiMajor(self):
        """Returns Semi Major of ellipse"""
        return self.semiMajor

    def getsemiMinor(self):
        """Returns Semi Minor of ellipse"""
        if self.y1 == self.y2:
            C2 = self.semiMajor**2
            B2 = (abs(self.x1 - self.x2) / 2)**2
            semiMinor = (C2 - B2)**0.5
        else:
            C2 = self.semiMajor**2
            B2 = (abs(self.y1 - self.y2) / 2)**2
            semiMinor = (C2 - B2)**0.5
        return semiMinor

    def minmaxx(self):
        """Returns the min and max X value for the ellipse"""
        semiMinor = self.getsemiMinor()
        if abs(self.y1 - self.y2) == 0:
            midx = abs(self.x1 - self.x2) / 2
            minx = round(midx - self.semiMajor, 4)
            maxx = round(midx + self.semiMajor, 4)
        else:
            minx = round(self.x1 - semiMinor, 4)
            maxx = round(self.x1 + semiMinor, 4)
        return minx, maxx

    def minmaxy(self):
        """Returns the min and max Y value for the ellipse"""
        semiMinor = self.getsemiMinor()
        if abs(self.x1 - self.x2) == 0:
            midy = abs(self.y1 - self.y2) / 2
            miny = round(midy - self.semiMajor, 4)
            maxy = round(midy + self.semiMajor, 4)
        else:
            miny = round(self.y1 - semiMinor, 4)
            maxy = round(self.y1 + semiMinor, 4)
        return miny, maxy

    def inside_edge(self, point):
        """returns True if a point is inside or on edge of ellipse"""
        pointdist = utility.distance(self.getFoci1(), point) + utility.distance(self.getFoci2(), point)
        if pointdist > self.semiMajor * 2:
            return False
        else:
            return True


# a = E(-1, 0, 1, 0, 3)
# print('semiMinor ', a.getsemiMinor())
# a.inside_edge((0, 2.9))
