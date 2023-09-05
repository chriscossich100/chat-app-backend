# Generated by Django 4.2.4 on 2023-08-26 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0015_alter_messages_chatroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Killer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('killerName', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='messages',
            name='chatroom',
            field=models.ManyToManyField(to='chatapp.killer'),
        ),
    ]
