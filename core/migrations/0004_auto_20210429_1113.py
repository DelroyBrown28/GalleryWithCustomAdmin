# Generated by Django 3.1.4 on 2021-04-29 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210429_1112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productlist',
            old_name='index_page_content',
            new_name='product_page_content',
        ),
    ]
