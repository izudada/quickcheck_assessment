# Generated by Django 3.2.15 on 2022-09-20 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='origin',
            field=models.CharField(default='hackernews', max_length=10),
        ),
    ]
