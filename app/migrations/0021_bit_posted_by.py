# Generated by Django 2.2.10 on 2020-03-04 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20200304_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='bit',
            name='posted_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bit', to='app.Member'),
        ),
    ]
