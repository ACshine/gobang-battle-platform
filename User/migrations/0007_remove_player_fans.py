# Generated by Django 4.1.2 on 2023-01-17 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0006_alter_player_fans"),
    ]

    operations = [
        migrations.RemoveField(model_name="player", name="fans",),
    ]
