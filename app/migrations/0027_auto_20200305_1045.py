# Generated by Django 2.2.10 on 2020-03-05 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20200305_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]