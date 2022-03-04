import os
import dotenv               # Always near the top!
dotenv.load_dotenv('.env')  # Load environment variables ASAP.


consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

from requests_oauthlib import OAuth1Session

session = OAuth1Session(consumer_key,
                      client_secret=consumer_secret,
                      resource_owner_key=access_token,
                      resource_owner_secret=access_token_secret)

# The URL endpoint to update a status (i.e. tweet)
url = 'https://api.twitter.com/2/tweets'


def tweet(message):
    resp = session.post(url, json={ 'text': message })
    return resp.text
