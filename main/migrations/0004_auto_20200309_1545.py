# Generated by Django 3.0.2 on 2020-03-09 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200308_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_products',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Order'),
        ),
        migrations.AlterField(
            model_name='order_products',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Product'),
        ),
    ]
