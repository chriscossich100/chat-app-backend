# Generated by Django 4.2.4 on 2023-09-05 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0032_alter_messages_datecreated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='description',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='messages',
            name='message',
            field=models.CharField(max_length=9000),
        ),
    ]
