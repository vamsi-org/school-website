# Generated by Django 2.1 on 2019-01-22 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20181208_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='fax_number',
        ),
    ]
