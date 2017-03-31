# Import our twitter credentials from credentials.py
import tweepy
from time import sleep
from credentials import *

# Access and authorize our twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open text file textfile.txt for reading
my_file = open('textfile.txt', 'r')

# Read lines one by one from my_file and assign to file_lines variable
file_lines = my_file.readlines()

# Close file
my_file.close()

# Tweet every hour
def tweet():
    for line in file_lines:
        try:
            print(line)
            # ensure blank lines are skipped
            if line != '\n':
                api.update_status(line)
                sleep(3600)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)
tweet()