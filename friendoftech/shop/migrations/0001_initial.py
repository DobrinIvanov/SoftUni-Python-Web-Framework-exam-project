# Generated by Django 4.1.3 on 2022-11-21 21:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('category', models.CharField(blank=True, choices=[('PHONES', 'Phones'), ('LAPTOPS', 'Laptops'), ('COMPUTERS_AND_COMPONENTS', 'Computers & Computer components'), ('SMART_WATCHES', 'Smart Watches'), ('PHOTOGRAPHY', 'Photography'), ('GAMING_CONSOLES', 'Gaming consoles'), ('HEADPHONES', 'Headphones'), ('TABLETS', 'Tablets'), ('AUDIO', 'Audio'), ('STORAGE', 'Storage')], max_length=50, null=True)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.TextField()),
                ('added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='shop.product')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(max_length=200)),
                ('is_positive', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]