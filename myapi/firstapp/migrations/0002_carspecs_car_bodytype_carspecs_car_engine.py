# Generated by Django 5.0.6 on 2024-06-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("firstapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="carspecs",
            name="car_bodytype",
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="carspecs",
            name="car_engine",
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
