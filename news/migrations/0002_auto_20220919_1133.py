# Generated by Django 3.2.15 on 2022-09-19 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='title',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='news',
            name='type',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
