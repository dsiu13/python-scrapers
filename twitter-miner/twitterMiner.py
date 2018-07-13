from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitterCreds

class TwitterStreamer():

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # Twitter authhandler & stream api
        listener = StdOutListener()
        auth = OAuthHandler(twitterCreds.CONSUMER_KEY, twitterCreds.CONSUMER_SECRET)
        auth.set_access_token(twitterCreds.ACCESS_TOKEN, twitterCreds.ACCESS_TOKEN_SECRET)

        stream = Stream(auth, listener)

        stream.filter(track=hash_tag_list)

class StdOutListener(StreamListener):

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
        return True
    except BaseException as e:
        print("Err on data: %s" str(e))
    return True

    def on_error(self, status):
        print(status)

if __name__ == "__main__":
    hash_tag_list = ['doge']
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
