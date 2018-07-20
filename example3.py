pi
#calculate  the circle's area
def circleArea(r):
    return r*r*pi

# add 2 for each element in the list
def addTwo(list):
    for i in range(len(list)):
        list[i]=list[i]+2
    return list

print(CircleArea(3))
resultantList = addTwo(['1','2','3'])
for i in resultantList:
    print(i)
