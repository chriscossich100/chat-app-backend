# Generated by Django 4.2.4 on 2023-08-26 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0016_killer_alter_messages_chatroom'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Killer',
        ),
        migrations.AlterField(
            model_name='messages',
            name='chatroom',
            field=models.ManyToManyField(to='chatapp.chatroom'),
        ),
    ]