# Generated by Django 4.2.4 on 2023-10-07 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cart', '0002_alter_cartitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
