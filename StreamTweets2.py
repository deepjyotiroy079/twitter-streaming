import tweepy 
from tweepy import OAuthHandler # to authenticate Twitter API
from tweepy import Stream 
from tweepy.streaming import StreamListener
import socket 
import json
import sys
import os
from dotenv import load_dotenv

load_dotenv()
# Twitter developer Credentials to connect to twitter account
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")
consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_SECRET")

# StreamListener class inherits from tweepy.StreamListener and overrides on_status/on_error methods.
class StreamListener(tweepy.StreamListener):

    def __init__(self, csocket):
        self.client_socket = csocket

    def on_data(self, data):
        try:
            msg = json.loads(data)
            print(msg['text'].encode('utf-8'))
            self.client_socket.send(msg['text'].encode('utf-8'))
            return True
        except BaseException as e:
            print('Error -> ', e)
    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        return True


def sendData(c_socket):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    streamListener = StreamListener(c_socket)
    stream = tweepy.Stream(auth=api.auth, listener=streamListener)
    stream.filter(track=["olympic"], languages=["en"])


if __name__ == "__main__":
   
    s = socket.socket()
    host = '127.0.0.1'
    port = 9999
    s.bind((host, port))
    print('Listening on port : %s' % port)
    # stream.filter(languages=["en"])
    s.listen(5)
 
    c, addr = s.accept()
    print('Received request from : %s' % str(addr))
    sendData(c)
