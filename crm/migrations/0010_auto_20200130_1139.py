# Generated by Django 3.0.2 on 2020-01-30 06:09

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_auto_20200130_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=phone_field.models.PhoneField(default='', help_text='Contact phone number', max_length=31),
        ),
    ]
