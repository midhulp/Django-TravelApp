# Generated by Django 3.2.12 on 2023-09-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
