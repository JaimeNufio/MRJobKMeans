import random

count = 500
xRange = 200 #Absolute
yRange = 200 #Absolute

random.seed()

with open("input.txt",'w') as file:
    for i in range(count):
        point = "{},{}\n".format(random.randrange(-xRange,xRange),random.randrange(-yRange,yRange))
        file.write(point);
