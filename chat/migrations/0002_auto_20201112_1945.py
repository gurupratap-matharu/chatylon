# Generated by Django 3.1.3 on 2020-11-12 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
