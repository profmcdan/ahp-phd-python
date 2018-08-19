# Generated by Django 2.0.2 on 2018-05-07 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ahp_app', '0006_auto_20180506_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ahp_app.Criteria'),
        ),
        migrations.AddField(
            model_name='bid',
            name='choices',
            field=models.TextField(blank=True, help_text='if the question type is "radio," "select," or "select multiple" provide a comma-separated list of options for this question .', null=True),
        ),
        migrations.AddField(
            model_name='bid',
            name='question_type',
            field=models.CharField(choices=[('text', 'text'), ('radio', 'radio'), ('select', 'select'), ('select-multiple', 'Select Multiple'), ('integer', 'integer')], default='text', max_length=200),
        ),
        migrations.AddField(
            model_name='bid',
            name='required',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='bid',
            name='text',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bid',
            name='temp_criteria',
            field=models.CharField(help_text='Enter multiple criteria separated by comma', max_length=400, null=True, verbose_name='Criteria'),
        ),
        migrations.AlterField(
            model_name='subcriteria',
            name='required',
            field=models.BooleanField(default=True),
        ),
    ]
