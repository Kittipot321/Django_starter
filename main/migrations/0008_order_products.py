# Generated by Django 3.0.2 on 2020-03-10 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200309_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='main.Order_Products', to='main.Product'),
        ),
    ]
