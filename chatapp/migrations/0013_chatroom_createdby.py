# Generated by Django 4.2.4 on 2023-08-21 19:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatapp', '0012_testermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='createdBy',
            field=models.ManyToManyField(blank=True, default=True, to=settings.AUTH_USER_MODEL),
        ),
    ]