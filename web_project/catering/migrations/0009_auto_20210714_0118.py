# Generated by Django 3.2.3 on 2021-07-13 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catering', '0008_auto_20210714_0050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_in',
            old_name='product_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product_in',
            old_name='p_price',
            new_name='price',
        ),
    ]
