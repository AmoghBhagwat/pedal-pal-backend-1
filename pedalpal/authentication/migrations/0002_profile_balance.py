# Generated by Django 4.2.10 on 2024-02-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="balance",
            field=models.IntegerField(default=0),
        ),
    ]
