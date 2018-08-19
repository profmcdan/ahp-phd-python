# Generated by Django 2.0.6 on 2018-07-28 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahp_app', '0011_auto_20180728_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='temp_criteria',
            field=models.CharField(choices=[('Financial Stability', 'Financial Stability'), ('Technical Capability', 'Technical Capability'), ('Past Performance', 'Past Performance'), ('Occupational Health & Safety', 'Occupational Health & Safety'), ('Management Capability', 'Management Capability'), ('Reputation', 'Reputation'), ('Experience  in Similar Project', 'Experience in Similar Project')], max_length=400, null=True, verbose_name='Select the appropriate criteria'),
        ),
    ]
