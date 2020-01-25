import base64
import requests
from KeyOps import KeyFetcher

from .models import *

class TweetSearcher:
    base_url = 'https://api.twitter.com/'
    client_key = ''
    client_secret = ''
    oAuthToken = ''

    def __init__(self, keysFile = "api_keys.txt"):
        kf = KeyFetcher()
        self.clientKey, self.clientSecret = kf.getKeys(keysFile)
        self.getOAuthToken()

    def getOAuthToken(self):
        key_secret = '{}:{}'.format(self.client_key, self.client_secret).encode('ascii')
        b64_encoded_key = base64.b64encode(key_secret)
        b64_encoded_key = b64_encoded_key.decode('ascii')

        auth_url = self.base_url + 'oauth2/token'

        auth_headers = {
            'Authorization': ('Basic '+b64_encoded_key),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }

        auth_data = {
            'grant_type': 'client_credentials'
        }

        auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

        self.access_token = auth_resp.json()['access_token']
    

    def searchTweets(self, searchname, type='all', count=500):
        search_headers = {
            'Authorization': ('Bearer '+self.access_token)    
        }


        if(type != 'all'):
            search_params = {
                'q': searchname,
                'result_type': type,
                'count': count
            }
        else:
            search_params = {
                'q': searchname,
                # 'result_type': type,
                'count': count
            }

        search_url = self.base_url+'1.1/search/tweets.json'

        search_resp = requests.get(search_url, headers=search_headers, params=search_params)

        if(search_resp.status_code == 200):
            tweets_dict = search_resp.json()
            return tweets_dict

        else:
            return None

class TweetFilterer:
    
    def __init__(self, tweets_dict):
        self.tweets_dict = tweets_dict

    def filterByLanguage(self, lang = 'en'):
        filtered_tweets = []

        for tweet in self.tweets_dict['statuses']:
            language = tweet['metadata']['iso_language_code']
            
            if(language == lang):
                filtered_tweets.append(tweet)
        
        return filtered_tweets

class TweetGetter:

    def getSearchwords(types = 'all'):
        entities = Entity.objects.all()

        searchwords = []

        for entity in entities:
            keywords.append(entity.name)
        
        return searchwords


    def getEnglishTweets():
        ts = TweetSearcher()
        tf = TweetFilterer()

        searchwords = getSearchwords()

        tweets = []

        for s in searchwords:
            pass #Start coding here