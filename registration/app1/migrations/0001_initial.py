# Generated by Django 5.0.1 on 2024-02-05 06:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Doctor",
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
                ("first_name", models.CharField(default="", max_length=30)),
                ("last_name", models.CharField(default="", max_length=30)),
                ("email", models.EmailField(max_length=254)),
                ("specialization", models.CharField(default="", max_length=100)),
                ("location", models.CharField(default="", max_length=100)),
                ("details", models.TextField(default="")),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="doctor_profile_pics/"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]