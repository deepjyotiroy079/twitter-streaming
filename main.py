from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext

conf = SparkConf().setAppName('Twitter-Streaming')

sc = SparkContext.getOrCreate(conf=conf)
sc.setLogLevel("ERROR")
ssc = StreamingContext(sc, 60)

## creating a socket stream
socket_stream = ssc.socketTextStream('127.0.0.1', 9999)


## create a window of 120 seconds
lines = socket_stream.window(120)

hashTags = lines.flatMap(lambda line: line.split(' ')).filter(lambda word: word.lower().startswith('#')).map(lambda z: (z.lower(), 1)).reduceByKey(lambda x,y: x+y)
# hashTags = lines.flatMap(lambda line: line.split(' ').

hashTags.pprint()

ssc.start()

ssc.awaitTermination()