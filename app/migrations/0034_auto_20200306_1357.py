# Generated by Django 2.2.10 on 2020-03-06 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_merge_20200306_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changelog',
            name='operation',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]