# Generated by Django 4.0.2 on 2022-03-16 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_ordermodel_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='total_price',
            field=models.FloatField(),
        ),
    ]
