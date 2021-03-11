# MRJob Solution: KMeans (First Itteration)

For my reference for a quick start-up. I'm sure it'll be useful to someone else eventually lol

## Creating Random Set of Missing Cards:

Initalize the points

Run `$ python3 createPoints.py`

## Prepping running on Hadoop:

Create the directory for input

Run `$ hdfs dfs -mkdir /user/jaime/mrJobKMeans`

Upload the input file to the input directory in HDFS

Run `$ hadoop fs -put input.txt /user/jaime/mrJobKMeans`

Create Output directory

Run `$ hadoop fs hdfs dfs -mkdir /user/jaime/outputMRJOBKMEANS`


## Run:
Run Python job in Hadoop

Run `$ python3 kmeans.py -r hadoop hdfs:///user/jaime/mrJobKMeans -o hdfs://outputMRJOBKMEANS --ctd input.txt`


## Get Results:
Run `$ hdfs dfs -cat hdfs:///outputMRJOBKMEANS/*`
