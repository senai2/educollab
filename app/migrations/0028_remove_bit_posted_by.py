# Generated by Django 2.2.10 on 2020-03-05 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20200305_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bit',
            name='posted_by',
        ),
    ]