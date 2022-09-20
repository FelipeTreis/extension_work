# Generated by Django 4.1.1 on 2022-09-20 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='automodel',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='brand',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]