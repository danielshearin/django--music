# Generated by Django 3.2.5 on 2021-07-19 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0023_alter_artist_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='published_date',
        ),
    ]
