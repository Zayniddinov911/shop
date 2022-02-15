# Generated by Django 4.0.2 on 2022-02-15 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='title')),
                ('collection', models.CharField(max_length=60, verbose_name='collection')),
                ('description', models.TextField(verbose_name='description')),
                ('banner', models.ImageField(upload_to='banners', verbose_name='banner')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
            ],
            options={
                'verbose_name': 'banner',
                'verbose_name_plural': 'banners',
            },
        ),
    ]