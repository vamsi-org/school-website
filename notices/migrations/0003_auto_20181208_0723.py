# Generated by Django 2.1 on 2018-12-08 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0002_notices_notice_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notices',
            name='notice_description',
            field=models.TextField(default=' ', max_length=600),
        ),
    ]
