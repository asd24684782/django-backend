# Generated by Django 4.0.8 on 2022-10-21 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_remove_contest_date_contest_cover_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contest",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="likes", to="core.profile"
            ),
        ),
        migrations.AlterField(
            model_name="contest",
            name="saved",
            field=models.ManyToManyField(
                blank=True, related_name="saved", to="core.profile"
            ),
        ),
    ]
