# Generated by Django 2.2.10 on 2020-03-04 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20200224_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
