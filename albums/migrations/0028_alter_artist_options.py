# Generated by Django 3.2.5 on 2021-07-21 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0027_alter_artist_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['artist']},
        ),
    ]