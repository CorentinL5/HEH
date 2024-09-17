""" exercice page 81
a = float(input("Insérez numéro 1:"))
b = float(input("Insérez numéro 2:"))

print(a + b)
print(a - b)
print(a * b)
print(round(a / b,2))
"""


""" exercice page 82
    x = float(input("entrer la valuer x:"))
    y= 1/(x+1/(x+(1/(x+(1/x)))))
    print("x=", x,"\ny=", y)
"""

""" exercice page 83
d = 0
h = int(input("entrez l'heure: "))
m = int(input("entrez les minutes: "))
t = int(input("entrez le temps: "))

while (m+t >= 60):
    h += 1
    t -= 60
while (h >= 24):
    h -= 24
    d += 1
print("days=>", d, ", hour=>", h, ":", (m+t)%60, sep="")
"""
"""
import math

h = int(input("entrez l'heure: "))
m = int(input("entrez les minutes: "))
t = int(input("entrez le temps: "))

print((h + math.floor((m+t)/60)%24), ":", (m+t)%60, sep="")
"""


