# Generated by Django 2.1.5 on 2019-03-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_listing_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='listing_pics/'),
        ),
    ]