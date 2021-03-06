# Generated by Django 2.2.10 on 2020-02-24 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20200224_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bit',
            name='file',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bit', to='app.File'),
        ),
        migrations.AlterField(
            model_name='member',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member', to='app.Institution'),
        ),
    ]
