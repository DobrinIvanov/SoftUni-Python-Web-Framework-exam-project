# Generated by Django 4.1.3 on 2022-12-15 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_messages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Messages',
            new_name='ClientMessage',
        ),
    ]