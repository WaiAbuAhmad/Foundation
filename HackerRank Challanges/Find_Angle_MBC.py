import math
AB= int(input())
BC = int(input())

CM= ((AB**(2)+BC**(2))**(0.5))/2



c=math.atan(AB/BC)
BM = ((BC**2+CM**2)-((2*BC*CM)*math.cos(c)))**(0.5)
b =round(math.degrees(math.acos(((BC**2+BM**2-CM**2)/(2*BM*BC)))))


print(b,chr(176),sep="")
