import math

degree_sign = u'\N{DEGREE SIGN}'

side_ab, side_bc = int(input()), int(input())
print(str(round(math.degrees(math.atan(side_ab/side_bc)))) + degree_sign)