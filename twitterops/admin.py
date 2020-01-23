from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Tweet)
admin.site.register(Entity)
admin.site.register(TweetEntities)
