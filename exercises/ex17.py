import math
def calc_lcm(a,b):
    gcd= math.gcd(a,b)
    lcm =(a*b)/gcd
    return lcm
a=12
b=36
lcm = calc_lcm(a,b)
print(f"LCM of {a},{b} is {lcm}")