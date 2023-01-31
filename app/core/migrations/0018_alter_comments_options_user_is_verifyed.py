# Generated by Django 4.0.8 on 2023-01-30 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_comments_content_alter_comments_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'get_latest_by': 'created_at', 'ordering': ['created_at'], 'verbose_name': '留言', 'verbose_name_plural': '留言'},
        ),
        migrations.AddField(
            model_name='user',
            name='is_verifyed',
            field=models.BooleanField(default=False),
        ),
    ]
