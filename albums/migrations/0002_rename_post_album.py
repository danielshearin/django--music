# Generated by Django 3.2.5 on 2021-07-16 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Album',
        ),
    ]
