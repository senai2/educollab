# Generated by Django 2.2.10 on 2020-02-24 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_upvote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='u_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL),
        ),
    ]
