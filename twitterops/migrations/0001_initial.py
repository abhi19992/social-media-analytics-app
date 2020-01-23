# Generated by Django 2.2.5 on 2020-01-23 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.IntegerField()),
                ('datetime', models.DateTimeField()),
                ('text', models.CharField(max_length=400)),
                ('user_id', models.IntegerField()),
                ('userName', models.CharField(max_length=20)),
                ('Sentiment', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TweetEntities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namedEntities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitterops.Entity')),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitterops.Tweet')),
            ],
        ),
    ]