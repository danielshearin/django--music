# Generated by Django 3.2.5 on 2021-07-19 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0011_auto_20210719_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
