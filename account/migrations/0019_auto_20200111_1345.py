# Generated by Django 2.2 on 2020-01-11 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_auto_20200111_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='subclass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.SubClass'),
        ),
    ]
