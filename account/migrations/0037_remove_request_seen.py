# Generated by Django 2.2 on 2020-03-12 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0036_auto_20200312_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='seen',
        ),
    ]
