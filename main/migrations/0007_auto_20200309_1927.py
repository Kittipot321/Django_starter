# Generated by Django 3.0.2 on 2020-03-09 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200309_1609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_products',
            old_name='order_id',
            new_name='order',
        ),
    ]
