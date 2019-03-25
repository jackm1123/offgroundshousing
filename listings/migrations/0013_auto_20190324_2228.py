# Generated by Django 2.1.5 on 2019-03-25 03:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0012_auto_20190324_2108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='is_active',
            new_name='active',
        ),
        migrations.AddField(
            model_name='listing',
            name='user_list',
            field=models.ManyToManyField(blank=True, related_name='user_favourite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='listing',
            name='favorite',
        ),
        migrations.AddField(
            model_name='listing',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]
