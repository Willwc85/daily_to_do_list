# Generated by Django 5.0.7 on 2024-08-04 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TimeField()),
                (
                    "done",
                    models.CharField(choices=[(1, "Doing"), (2, "Done")], max_length=1),
                ),
            ],
        ),
    ]
