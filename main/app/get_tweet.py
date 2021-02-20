from key_seq import keys
import tweepy
import datetime

dt_now = datetime.datetime.now()

tokens = keys
today_dt = dt_now.strftime('%Y-%m-%d')

consumer_key, consumer_secret, access_token, access_token_secret = tokens.get_tokens(tokens)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

get_list = [tweet for tweet in tweepy.Cursor(api.user_timeline, id="UsuwoLaboratory").items(1)]

for text in get_list:
    if text.created_at.strftime('%Y-%m-%d') == today_dt:
        print(text.text)