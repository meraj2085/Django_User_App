# Generated by Django 4.1.5 on 2023-01-23 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UserApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="UserEmail",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]