# Generated by Django 4.0.2 on 2022-02-19 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_productmodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
            },
        ),
        migrations.AddField(
            model_name='productmodel',
            name='brand',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, related_name='products', to='shop.brandingmodel', verbose_name='brand'),
            preserve_default=False,
        ),
    ]
