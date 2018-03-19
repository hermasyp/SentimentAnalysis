
import tweepy
#Twitter Configuration
CONSUMER_KEY    = 'ivZxDXj7bc26e1HUbBbVAFlwN'
CONSUMER_SECRET = 'hI9YQeJo6FatoVNJyY4HZgjMic61dpFUPAo6DUkdVvl17IEoIC'

# Access Configuration:
ACCESS_TOKEN  = '68413536-WpYNwsQg1NwRq4rnUx6ZP332HOc7znHh297TCw3sk'
ACCESS_SECRET = 'Eajelt5yz1NaYtHHGq0EOzRIv9Xk81JXWWmQ4U1ihfCjO'


def twitter_init():

    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api