# Generated by Django 4.1.5 on 2023-01-28 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ArticaleApp", "0004_rename_reporter_article_reporter_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article",
            old_name="reporter_Id",
            new_name="reporter",
        ),
    ]