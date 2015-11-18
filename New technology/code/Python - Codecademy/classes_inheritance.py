class Triangle(object):
    
    number_of_sides = 3
    
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False

my_triangle = Triangle(90, 30, 60)

print "Triangle"
print my_triangle.number_of_sides
print my_triangle.check_angles()

class Equilateral(Triangle):
    angle = 60
    
    def __init__(self):
        self.angle1 = 60
        self.angle2 = 60
        self.angle3 = 60

my_equilateral = Equilateral()

print ""
print "Equilateral"
print my_equilateral.number_of_sides
print my_equilateral.check_angles()
print "Angles: %s %s %s" % (my_equilateral.angle1, my_equilateral.angle2, my_equilateral.angle3)
