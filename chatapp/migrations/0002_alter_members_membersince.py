# Generated by Django 4.2.4 on 2023-08-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='memberSince',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
