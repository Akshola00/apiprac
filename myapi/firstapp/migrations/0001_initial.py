# Generated by Django 5.0.6 on 2024-06-27 18:13

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CarSpecs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("car_model", models.TextField(max_length=200)),
                ("car_year", models.TextField(max_length=200)),
                ("car_type", models.TextField(max_length=200)),
            ],
        ),
    ]
