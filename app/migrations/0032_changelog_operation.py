# Generated by Django 2.2.8 on 2020-03-05 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20200305_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='changelog',
            name='operation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
