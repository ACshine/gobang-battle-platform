# Generated by Django 4.1.2 on 2023-01-17 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0002_player_delete_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="fans",
            field=models.ManyToManyField(to="User.player"),
        ),
    ]
