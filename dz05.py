# This is 5th homework of the Phyton course from http://dswz.ru
#
# Создан класс Самолет, от него унаследованы два других класса - Боинг и Аирбас
# В небе размера 25*25 создано 50 самолетов со случайными координатами, пропорция между Боингами и Аирбасами тоже случайная
# Выбирается произвольный самолет и ищется ближайший к нему. Результаты выводятся в mainframe-style text drawing ;)

class Airplane:
    def __init__ (self, tailnumber, cx, cy):
        self.tailnumber = tailnumber
        self.cx = cx
        self.cy = cy
    def distfrom(self, dx, dy):
        return (math.sqrt(((dx-self.cx) ** 2) + (dy-self.cy) ** 2))

class Boeing(Airplane):
    def my_name(self):
        return "B"
 
class Airbus(Airplane):
    def my_name(self):
        return "A"

import random
import math

GRIDSIZE = 25
PLANECOUNT = 50

# инициализация
l = list()
n = random.randint(1,PLANECOUNT+1)
for i in range(1, n):
    c = Airbus("AP"+str(i), random.randint(1,GRIDSIZE+1), random.randint(1,GRIDSIZE+1))
    l.append(c)
for i in range(n,PLANECOUNT+1):
    c = Boeing("AP"+str(i), random.randint(1,GRIDSIZE+1), random.randint(1,GRIDSIZE+1))
    l.append(c)

# берем произвольный самолет
one = l[random.randint(1,PLANECOUNT+1)]
print("Выбран борт", one.tailnumber, "с координатами {0}:{1}".format(one.cx, one.cy))

# ищем ближайший к нему
dmin = GRIDSIZE
for i in range(PLANECOUNT):
    if (one.distfrom(l[i].cx,l[i].cy) < dmin) and (one.tailnumber != l[i].tailnumber):
        dmin = one.distfrom(l[i].cx,l[i].cy)
        another = l[i]
print ("Ближайший к нему борт", another.tailnumber, "с координатами {0}:{1}\n".format(another.cx, another.cy))

# распечатка 'неба' с самолетами
ln = "+  "
for a in range (1,GRIDSIZE+1):
    s = str(a)
    while len(s) < 3:
        s = s + " "
    ln = ln + s
print(ln)
for a in range (1,GRIDSIZE+1):
    s = str(a)
    while len(s) < 3:
        s = s + " "
    for b in range (1,GRIDSIZE+1):
        found = False
        for c in range (PLANECOUNT):
            if l[c].distfrom(a,b) == 0:
                if found == True:
                    s = s[0:len(s)-4] + "(*) "
                else:
                    found = True
                    if l[c].tailnumber == one.tailnumber:
                        s = s[0:len(s)-1] + "[" + l[c].my_name() + "] "
                    elif l[c].tailnumber == another.tailnumber:
                        s = s[0:len(s)-1] + "{" + l[c].my_name() + "} "
                    else:
                        s = s + l[c].my_name() + "  "
        if found == False:
            s = s + "-  "
    print(s)