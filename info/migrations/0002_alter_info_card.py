# Generated by Django 4.1.1 on 2022-10-04 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="info",
            name="card",
            field=models.CharField(max_length=12),
        ),
    ]