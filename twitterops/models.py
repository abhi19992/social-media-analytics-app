from django.db import models
import datetime

# Create your models here.
class Tweet(models.Model):
    tweet_id = models.IntegerField()
    datetime = models.DateTimeField()
    text = models.CharField(max_length = 400)
    user_id = models.IntegerField()
    userName = models.CharField(max_length=20)
    Sentiment = models.IntegerField(default = 0)

    def __str__(self):
        return self.datetime + ' - ' + self.tweet_id

class Entity(models.Model):
    name = models.CharField(max_length = 30)
    type = models.CharField(max_length = 40, default='')

    def __str__(self):
        return self.name

class TweetEntities(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    namedEntity = models.ForeignKey(Entity, on_delete=models.CASCADE)

    def __str__(self):
        return self.tweet.tweet_id + ' - ' + self.namedEntities
