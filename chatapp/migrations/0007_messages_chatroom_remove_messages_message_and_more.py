# Generated by Django 4.2.4 on 2023-08-17 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0006_remove_chatroom_message_remove_messages_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='chatroom',
            field=models.ManyToManyField(blank=True, null=True, to='chatapp.chatroom'),
        ),
        migrations.RemoveField(
            model_name='messages',
            name='message',
        ),
        migrations.AddField(
            model_name='messages',
            name='message',
            field=models.CharField(default=7, max_length=950),
            preserve_default=False,
        ),
    ]