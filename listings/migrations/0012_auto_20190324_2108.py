# Generated by Django 2.1.5 on 2019-03-25 02:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0011_auto_20190324_0310'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dummyfield', models.IntegerField(default=5)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='user_favourite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='listing',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
