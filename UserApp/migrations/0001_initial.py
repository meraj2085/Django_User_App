# Generated by Django 4.1.5 on 2023-01-16 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                ("UserId", models.AutoField(primary_key=True, serialize=False)),
                ("UserName", models.CharField(max_length=100)),
                ("UserEmail", models.CharField(max_length=100)),
            ],
        ),
    ]