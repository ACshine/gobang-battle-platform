# Generated by Django 4.1.2 on 2023-01-17 05:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("User", "0004_alter_player_fans"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="fans",
            field=models.ManyToManyField(
                related_name="fan_s", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
