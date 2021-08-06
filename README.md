# twitter-streaming 

- This project aims to count hashtags that are currently tweeted on Twitter. The data is collected for 60 seconds with a processing window of 120 seconds.
- Makes use of the [Twitter API](https://developer.twitter.com/en/docs), [Spark Streaming](https://spark.apache.org/docs/latest/streaming-programming-guide.html) and Python.

## Prerequisites

Make sure you have Spark set up on your local machine.

Creata a virtual environment

```bash
python -m venv myvenv
```

Install dependencies

```bash
pip install python-dotenv tweepy
```

## Execution

1. Open a terminal and run the ```main.py```

```bash
python main.py
```

2. Open up another terminal and submit ```StreamTweets2.py``` to spark-submit on ```127.0.0.1``` and port ```9999```.

```cmd
%SPARK_HOME%\bin\spark-submit <path to the StreamTweets2.py file> 127.0.0.1 9999
```

## Result

```bash
-------------------------------------------
Time: 2021-08-05 21:31:00
-------------------------------------------
('#esp', 2)
('#menshockeyteam', 5)
('#cuba', 1)
('#olympic', 4)
('#teamusatf', 2)
('#uswnt', 2)
('#tokyo20àrt', 1)
('#wrestletàrt', 1)
('#tokyo2020', 8)
('#silver', 2)
...

-------------------------------------------
Time: 2021-08-05 21:32:00
-------------------------------------------
('#esp', 2)
('#menshockeyteam', 11)
('#cuba', 1)
('#olympic', 6)
('#teamusatf', 2)
('#uswnt', 2)
('#tokyo20àrt', 1)
('#wrestletàrt', 1)
('#tokyo2020', 20)
('#silver', 3)
...
```

## Issues

Unable to read some characters present in the tweets, due the which the program throws the below error

```bash
UnicodeEncodeError: 'charmap' codec can't encode characters in position 3-7: character maps to <undefined>
```
