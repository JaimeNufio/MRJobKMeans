import random

count = 500
xRange = 200 #Absolute
yRange = 200 #Absolute

random.seed()

K = 3
Centroids = [] 

with open("input.txt",'w') as file:
    for i in range(count):
        point = "{},{}\n".format(random.randrange(-xRange,xRange),random.randrange(-yRange,yRange))

        if i < K:
            # all these points are created at random, so collecting the first 3 is
            # all we need for 'random' points
            Centroids.append(point)

        file.write(point)

with open("Centroids.txt",'w') as file:
    for i in range(K):
        file.write(Centroids[i])
