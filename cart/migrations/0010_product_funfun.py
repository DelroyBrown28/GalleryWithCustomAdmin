# Generated by Django 3.1.4 on 2021-01-19 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_auto_20201218_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='funfun',
            field=models.FileField(default=False, upload_to='media'),
        ),
    ]
