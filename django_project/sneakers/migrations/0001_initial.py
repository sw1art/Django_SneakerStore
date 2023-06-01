# Generated by Django 4.2 on 2023-06-01 19:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=400, null=True)),
                ('logo', models.ImageField(default='brand_logos/default.png', upload_to='brand_logos/')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_us', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('size_ru', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('size_eu', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('size_uk', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('size_cm', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'Размеры',
            },
        ),
        migrations.CreateModel(
            name='Sneaker',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300, unique=True)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('feature', models.TextField(blank=True, max_length=500, null=True)),
                ('price', models.DecimalField(decimal_places=0, max_digits=7)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(default='sneaker_images/default.jpg', upload_to='sneaker_images/')),
                ('slug', models.SlugField(max_length=310, unique=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sneakers.brand')),
                ('sizes', models.ManyToManyField(to='sneakers.size')),
            ],
            options={
                'verbose_name': 'Кроссовки',
                'verbose_name_plural': 'Кроссовки',
            },
        ),
    ]
