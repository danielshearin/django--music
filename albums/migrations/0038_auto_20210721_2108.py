# Generated by Django 3.2.5 on 2021-07-21 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0037_alter_album_artist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['artist']},
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='album_artist',
            new_name='artist',
        ),
    ]
