# Generated by Django 3.1.4 on 2020-12-13 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sizevariation',
            name='size_price',
            field=models.IntegerField(default=0),
        ),
    ]