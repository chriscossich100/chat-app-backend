# Generated by Django 4.2.4 on 2023-08-26 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0018_killer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='chatroom',
            field=models.ManyToManyField(to='chatapp.killer'),
        ),
    ]