# Generated by Django 2.0.2 on 2018-05-06 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahp_app', '0005_auto_20180506_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='temp_criteria',
            field=models.CharField(max_length=400, null=True, verbose_name='Criteria'),
        ),
    ]
