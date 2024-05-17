import numpy
import time
import os
rows = []
p = int(input())
z = int(input())
super = numpy.empty((p,z), dtype='<U10')

for i in range(p):
    for j in range(z):
        super[i][j]="_"

def place(coordinatex, coordinatey):
    super[coordinatex][coordinatey]="X"

def remove(coordinatex, coordinatey):
    super[coordinatex][coordinatey]="_"

def functionprint():
    for i in range(p):
        for j in range(z):
            print(super[p-i-1][j], end ="")
        print(" ")

def search(x,y,array):
    neighbours = 0
    x_size = len(array[0])
    y_size = len(array)
    #tehse are the normal axes
    if x+1<x_size and array[y][x+1]=="X":
        neighbours+=1
    if x-1>=0 and array[y][x-1]=="X":
       neighbours+=1
    if y-1>=0 and array[y-1][x]=="X":
       neighbours+=1
    if y+1<y_size and array[y+1][x]=="X":
       neighbours+=1
    # these are going to be the diagonals now
    if x+1<x_size and y+1<y_size and array[y+1][x+1]=="X":
        neighbours+=1
    if x-1>=0 and y+1<y_size and array[y+1][x-1]=="X":
        neighbours+=1
    if x+1<x_size and y-1>=0 and array[y-1][x+1]=="X":
        neighbours+=1
    if x-1>=0 and y-1>=0 and array[y-1][x-1]=="X":
        neighbours+=1
    else:
        neighbours= neighbours
    return neighbours


print("Now input the coordinates of where you want the starting squares to be located (to leave this enter a negative coordinate)")
coords = input("coordinates: ")
y,x = (coords.split(" "))
x = int(x)
y = int(y)
if (x>=0 and y>=0):
    place(x,y)
while (x>=0 and y>=0):
    coords = input("coordinates: ")
    y,x = (coords.split(" "))
    x = int(x)
    y = int(y)
    if (x>=0 and y>=0):
        place(x,y)
    functionprint()

placeholder = numpy.empty((p,z), dtype='<U10')

while(True):
    for i in range(p):
        for j in range(z):
            if super[i][j]=="X":
               holder = search(i,j,super)
               if holder <= 1:
                  placeholder[i][j]="_"
               if holder >= 4:
                  placeholder[i][j]="_"
               else:
                  placeholder[i][j]="X"
            else:
                holder = search(i,j,super)
                if holder ==3:
                    placeholder[i][j]="X"
                else:
                    placeholder[i][j]="_"
    super = placeholder
    placeholder = numpy.empty((p,z), dtype='<U10')
    os.system("clear")
    functionprint()
    time.sleep(3)
