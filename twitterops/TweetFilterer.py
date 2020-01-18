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