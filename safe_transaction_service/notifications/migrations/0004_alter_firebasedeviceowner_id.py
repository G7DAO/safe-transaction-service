# Generated by Django 3.2.4 on 2021-06-07 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notifications", "0003_firebasedeviceowner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="firebasedeviceowner",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
