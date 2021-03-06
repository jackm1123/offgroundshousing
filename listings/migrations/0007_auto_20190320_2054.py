# Generated by Django 2.1.7 on 2019-03-21 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20190320_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='latitude',
            field=models.DecimalField(decimal_places=3, default=38.034, max_digits=6),
        ),
        migrations.AlterField(
            model_name='listing',
            name='longitude',
            field=models.DecimalField(decimal_places=3, default=78.508, max_digits=6),
        ),
    ]
