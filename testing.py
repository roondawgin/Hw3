import utility, EllipseClass, main

print('Functions in utility.py')
print('******distance******')
print('returns distance between 2 points')
print('testing with 2 points left of y axis')
print('utility.distance((-5, -3), (-10, -3))')
print(utility.distance((-5, -3), (-10, -3)))
print()
print('testing with 1 point left of y axis and one on the right')
print('utility.distance((-5, -3), (10, 3))')
print(utility.distance((-5, -3), (10, 3)))
print()
print('******circumference******')
print('returns circumference of ellipse')
print('testing with different semi major and semi minor')
print('utility.circumference(1, 2)')
print(utility.circumference(1, 2))
print()
print('testing with same semi major and semi minor')
print('utility.circumference(1, 1)')
print(utility.circumference(1, 1))
print()
print('******area******')
print('Returns approximate area of ellipse')
print('testing with different semi major and semi minor')
print('utility.area(1, 2)')
print(utility.area(1, 2))
print()
print('testing with same semi major and semi minor')
print('utility.area(1, 1)')
print(utility.area(1, 1))
print()
print('Functions in EllipseClass.py')
print('******Ellipse Class******')
print('Defines and edits ellipse objects based on 2 foci and the Semi Major')
print('testing with allowed parameters')
print('EllipseClass.Ellipse(0, 0, 1, 0, 2)')
print(EllipseClass.Ellipse(0, 0, 1, 0, 2))
print()
print('testing with string in x1')
print('EllipseClass.Ellipse(\'string\', 0, 1, 0, 2)')
try:
    print(EllipseClass.Ellipse('string', 0, 1, 0, 2))
except:
    print('TypeError')
print()
print('testing with string in y1')
print('EllipseClass.Ellipse(0,  \'string\', 1, 0, 2)')
try:
    print(EllipseClass.Ellipse(0, 'string', 1, 0, 2))
except:
    print('TypeError')
print()
print('testing with string in x2')
print('EllipseClass.Ellipse(0, 0, \'string\', 0, 2)')
try:
    print(EllipseClass.Ellipse(0, 0, 'string', 0, 2))
except:
    print('TypeError')
print()
print('testing with string in y2')
print('EllipseClass.Ellipse(0, 0, 1, \'string\', 2)')
try:
    print(EllipseClass.Ellipse(0, 0, 1, 'string', 2))
except:
    print('TypeError')
print()
print('testing with string in semi Major')
print('EllipseClass.Ellipse(0, 0, 1, 0, \'string\')')
try:
    print(EllipseClass.Ellipse(0, 0, 1, 0, 'string'))
except:
    print('TypeError')
print()
print('testing with semi Major and both X\'s and Y\'s different')
print('EllipseClass.Ellipse(1, 2, 3, 4, 4)')
try:
    print(EllipseClass.Ellipse(1, 2, 3, 4, 4))
except:
    print('ValueError')
print()
print('testing with negative semi Major')
print('EllipseClass.Ellipse(1, 2, 3, 4, -4)')
try:
    print(EllipseClass.Ellipse(1, 2, 3, 4, -4))
except:
    print('ValueError')
print()