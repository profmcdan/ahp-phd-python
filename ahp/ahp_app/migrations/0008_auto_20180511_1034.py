# Generated by Django 2.0.2 on 2018-05-11 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahp_app', '0007_auto_20180507_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='activated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bid',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]