# Generated by Django 2.0.2 on 2018-05-02 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahp_app', '0002_auto_20180502_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='conditions',
        ),
        migrations.RemoveField(
            model_name='response',
            name='interviewee',
        ),
        migrations.AlterField(
            model_name='response',
            name='interviewer',
            field=models.CharField(max_length=400, verbose_name='Name of Decision Maker'),
        ),
    ]