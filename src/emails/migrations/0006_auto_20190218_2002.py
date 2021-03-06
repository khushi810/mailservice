# Generated by Django 2.0.7 on 2019-02-18 20:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0005_auto_20190218_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='email',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
