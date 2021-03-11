from mrjob.job import MRJob
import math
import os
import sys

class MRKMeans(MRJob):

    def configure_args(self):
        super(MRKMeans, self).configure_args()
        self.add_file_arg('--ctd')

    def mapper_init(self):
        self.centroids = []
        with open(self.options.ctd,'r') as f:
            for line in f:
                cent = line.split(",")
                self.centroids.append( (int(cent[0]),int(cent[1])) )

    def dist(self,v1,v2):
        #v1 and v2 are tuples
        return math.sqrt( ((v1[0]-v2[0])**(2))+((v1[1]-v2[1])**2) )

    def classify(self,centroids,v):
        minDist = 99999999
        which = -1
        itr = 0
        for vector in centroids:
            itr+=1
            currDist = self.dist(vector,v)
            if currDist < minDist:
                minDist = currDist
                which = itr
        return str(which)

    def mapper(self,_,line):
        (X,Y) = line.split(',')
        X = int(X)
        Y = int(Y)

        yield self.classify(self.centroids,(X,Y)),"{},{}".format(X,Y)

    def reducer(self, K, pairs):
        All = ""
        SumX = 0
        SumY = 0
        Num = 0

        for item in pairs:
            pair = item.split(",")
            SumX = int(pair[0])
            SumY = int(pair[1])
            Num+=1

        yield K, "({},{})".format(SumX/Num,SumY/Num)

        #yield K,(list(pair))

if __name__ == '__main__':
    MRKMeans.run()
