# MRJob Solution: KMeans (First Itteration)

For my reference for a quick start-up. I'm sure it'll be useful to someone else eventually lol

## Creating Random Set of Missing Cards:

Initalize the points

Run `$ python3 createPoints.py`

## Prepping running on Hadoop:

Create the directory for input

Run `$ hdfs dfs -mkdir /user/jaime/allPoints`

Upload the input file to the input directory in HDFS

Run `$ hdfs dfs -put ./input.txt hdfs:/user/jaime/allPoints`

Create Output directory

Run `$ hdfs dfs -rmdir /user/jaime/newCluster`


## Run:
Run Python job in Hadoop:

Run `$ python3 kmeans.py -r hadoop hdfs:///user/jaime/allPoints/input.txt -o hdfs:///user/jaime/newCluster --ctd ./Centroids.txt`


## Get Results:
Run `$ hdfs dfs -cat /user/jaime/newCluster/*`

Output should be something like:
```
"1"	"(-0.8051948051948052,0.6948051948051948)"
"2"	"(1.434782608695652,0.050724637681159424)"
"3"	"(0.08653846153846154,-0.24519230769230768)"
```