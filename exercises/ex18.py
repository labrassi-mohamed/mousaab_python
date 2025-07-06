import math
def calc_area (sidea ,sideb,sidec):
    semi_perimeter =(sidea+sideb+sidec)/2
    area_sq= semi_perimeter*(semi_perimeter-sidea)*(semi_perimeter-sideb)*(semi_perimeter-sidec)
    return math.sqrt(area_sq)
sidea= input ("Enter length of side 1 : ")
sideb= input ("Enter length of side 2 : ")
sidec= input ("Enter length of side 3 : ")
area =calc_area (int(sidea),int(sideb),int(sidec))
print (f"the area is {area}")

