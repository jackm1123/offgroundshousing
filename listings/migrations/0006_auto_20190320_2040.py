# Generated by Django 2.1.7 on 2019-03-21 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_listing_pictures'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='latitude',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='listing',
            name='longitude',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
    ]
