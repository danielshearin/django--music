# Generated by Django 3.2.5 on 2021-07-19 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0013_alter_album_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='artist_name',
            new_name='artist',
        ),
    ]
