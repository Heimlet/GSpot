# Generated by Django 4.2.2 on 2023-06-13 15:20

import customer.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("customer", "0003_remove_customeruser_last_login"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customeruser",
            managers=[
                ("objects", customer.models.CustomerManager()),
            ],
        ),
    ]