# Generated by Django 4.0.2 on 2022-02-17 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(default=None, upload_to='products', verbose_name='image'),
            preserve_default=False,
        ),
    ]
