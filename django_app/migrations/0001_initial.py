# Generated by Django 5.1.7 on 2025-03-21 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StockData",
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
                ("timestamp", models.DateTimeField()),
                ("open_price", models.FloatField()),
                ("close_price", models.FloatField()),
                ("high", models.FloatField()),
                ("low", models.FloatField()),
            ],
        ),
    ]
