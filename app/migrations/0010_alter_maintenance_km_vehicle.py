# Generated by Django 4.1.1 on 2022-11-18 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0009_alter_automodel_name_alter_brand_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="maintenance",
            name="km_vehicle",
            field=models.IntegerField(default=0),
        ),
    ]
