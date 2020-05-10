# Generated by Django 2.2.7 on 2020-01-28 03:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0002_auto_20200125_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=254)),
                ('mobile', phone_field.models.PhoneField(blank=True, default='', help_text='Contact phone number', max_length=31)),
                ('name', models.CharField(default='', max_length=50)),
                ('area', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='crm.Area')),
                ('city', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='crm.City')),
                ('state', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='crm.State')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('price', models.FloatField()),
                ('category', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('date_created', models.DateTimeField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out of Delivery', 'Out of Delivery'), ('Deliverd', 'Deliverd')], max_length=50, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer')),
                ('product', models.ManyToManyField(to='crm.Product')),
            ],
        ),
    ]
