# Generated by Django 2.2.8 on 2019-12-04 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20191204_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10, max_length=32),
        ),
    ]
