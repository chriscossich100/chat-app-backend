# Generated by Django 4.2.4 on 2023-08-17 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0005_messages_chatroom_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='message',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='message',
        ),
        migrations.AddField(
            model_name='messages',
            name='message',
            field=models.ManyToManyField(blank=True, null=True, to='chatapp.chatroom'),
        ),
    ]