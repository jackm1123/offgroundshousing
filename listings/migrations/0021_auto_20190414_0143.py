# Generated by Django 2.1.5 on 2019-04-14 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0020_auto_20190414_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='cached_latitude',
            field=models.FloatField(default=-1),
        ),
        migrations.AlterField(
            model_name='listing',
            name='cached_longitude',
            field=models.FloatField(default=-1),
        ),
    ]
