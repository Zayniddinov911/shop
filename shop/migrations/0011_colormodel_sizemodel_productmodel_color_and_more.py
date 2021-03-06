# Generated by Django 4.0.2 on 2022-02-22 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_remove_productmodel_brand_delete_brandingmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=7, verbose_name='color')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'color',
                'verbose_name_plural': 'colors',
            },
        ),
        migrations.CreateModel(
            name='SizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'size',
                'verbose_name_plural': 'sizes',
            },
        ),
        migrations.AddField(
            model_name='productmodel',
            name='color',
            field=models.ManyToManyField(null=True, related_name='products', to='shop.ColorModel', verbose_name='color'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='size',
            field=models.ManyToManyField(null=True, related_name='products', to='shop.SizeModel', verbose_name='size'),
        ),
    ]
