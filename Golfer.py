'''
Author: Jesse Greenlee
Purpose of Program: To enter golfers into a database and keep track of yardage per club (Driver-Lob Wedge)

Golfer Class has 13 properties:
f_name: First Name
l_name: Last Name
driver: Distance
three_wood: Distance
hybrid: Distance
five_iron: Distance
six_iron: Distance
seven_iron: Distance
eight_iron: Distance
nine_iron: Distance
p_wedge: Distance
s_wedge: Distance
l_wedge: Distance
golfer_id: This is an optional parameter. Database will create automatically with auto increment
'''

class Golfer:
    def __init__(self, f_name, l_name, driver, three_wood, hybrid, five_iron, six_iron, seven_iron, eight_iron, nine_iron, p_wedge, s_wedge,l_wedge, golfer_id=None):
        self.f_name = f_name
        self.l_name = l_name
        self.driver = driver
        self.three_wood = three_wood
        self.golfer_id = golfer_id
        self.hybrid = hybrid
        self.five_iron = five_iron
        self.six_iron = six_iron
        self.seven_iron = seven_iron
        self.eight_iron = eight_iron
        self.nine_iron = nine_iron
        self.p_wedge = p_wedge
        self.s_wedge = s_wedge
        self.l_wedge = l_wedge

    def __str__(self):
        return f' Name: {self.f_name} {self.l_name},  Driver: {self.driver},  3 Wood: {self.three_wood}, Hybrid: {self.hybrid}, 5-iron: {self.five_iron}, 6-iron: {self.six_iron}, 7-iron: {self.seven_iron}, 8-iron: {self.eight_iron}, 9-iron: {self.nine_iron}, Wedge: {self.p_wedge}, Sandy: {self.s_wedge}, Lob: {self.l_wedge}, ID: {self.golfer_id} '