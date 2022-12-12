# Generated by Django 4.0.8 on 2022-10-30 14:43

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("core", "0013_alter_artist_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contest",
            name="tags",
        ),
        migrations.AddField(
            model_name="contest",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]