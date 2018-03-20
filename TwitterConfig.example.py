
import tweepy
#Twitter Configuration
CONSUMER_KEY    = ''
CONSUMER_SECRET = ''

# Access Configuration:
ACCESS_TOKEN  = ''
ACCESS_SECRET = ''


def twitter_init():

    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api