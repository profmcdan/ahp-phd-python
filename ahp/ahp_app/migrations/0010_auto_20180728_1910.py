# Generated by Django 2.0.6 on 2018-07-28 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ahp_app', '0009_auto_20180511_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectType', models.FileField(null=True, upload_to='projectType/', verbose_name='Type of Past Projects Completed')),
                ('projectSize', models.FileField(null=True, upload_to='projectSize/', verbose_name='Size of Past Projects Completed')),
                ('numProjext', models.FileField(null=True, upload_to='numProjext/', verbose_name='Number of Past Projects Completed')),
                ('localAreaExperience', models.FileField(null=True, upload_to='localAreaExperience/', verbose_name='Experience in Local Area')),
                ('contractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ahp_app.Contractor')),
            ],
        ),
        migrations.CreateModel(
            name='FinancialStability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soundness', models.FileField(null=True, upload_to='soundness/', verbose_name='Financial Soundness')),
                ('credit_rating', models.FileField(null=True, upload_to='credit_rating/', verbose_name='Financial Credit Rating')),
                ('banking_bonding', models.FileField(null=True, upload_to='banking_bonding/', verbose_name='Financial Arrangements and Bonding')),
                ('status', models.FileField(null=True, upload_to='status/', verbose_name='Financial Status')),
                ('liquidity', models.FileField(null=True, upload_to='liquidity/', verbose_name='Financial Liquidity')),
                ('contractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ahp_app.Contractor')),
            ],
        ),
        migrations.CreateModel(
            name='ManagementCapability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualityPolicy', models.FileField(null=True, upload_to='qualityPolicy/', verbose_name='Quality Policy')),
                ('projectManagement', models.FileField(null=True, upload_to='projectManagement/', verbose_name='Project Management Organization')),
                ('culture', models.FileField(null=True, upload_to='culture/', verbose_name='Organizational Culture')),
                ('knowledge', models.FileField(null=True, upload_to='knowledge/', verbose_name='Management Knowledge')),
                ('contractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ahp_app.Contractor')),
            ],
        ),
        migrations.CreateModel(
            name='OccupationalHS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('healthSafety', models.FileField(null=True, upload_to='healthSafety/', verbose_name='Health and Safety Performance Report')),
                ('safety', models.FileField(null=True, upload_to='safety/', verbose_name='Occupational Safety and Health Administration Procedures')),
                ('generalAssessment', models.FileField(null=True, upload_to='generalAssessment/', verbose_name='General Assessment of Safety Attitudes')),
                ('contractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ahp_app.Contractor')),
            ],
        ),
        migrations.CreateModel(
            name='PastPerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.FileField(null=True, upload_to='quality/', verbose_name='Quality Level of Project Performance')),
                ('completedTime', models.FileField(null=True, upload_to='completionTime/', verbose_name='Projects Completed on Time')),
                ('completedBudjet', models.FileField(null=True, upload_to='completedBudjet/', verbose_name='Projects Completed on Budget')),
                ('contractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ahp_app.Contractor')),
            ],
        ),
        migrations.CreateModel(
            name='Reputation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('failures', models.FileField(null=True, upload_to='failures/', verbose_name='Past Failures')),
                ('timeInBusiness', models.FileField(null=True, upload_to='timeInBusiness/', verbose_name='Length of time in Business')),
                ('pastOwner', models.FileField(null=True, upload_to='pastOwner/', verbose_name='Past Owner / Contractor Relationship')),
                ('relationships', models.FileField(null=True, upload_to='relationships/', verbose_name='Other Relationships')),
                ('contractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ahp_app.Contractor')),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalCapability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.FileField(null=True, upload_to='experience/', verbose_name='Experience of Technical Personnels')),
                ('labour', models.FileField(null=True, upload_to='labour/', verbose_name='Labour and Equipment')),
                ('qualification', models.FileField(null=True, upload_to='qualification/', verbose_name='Qualification of Personnels')),
                ('ability', models.FileField(null=True, upload_to='ability/', verbose_name='Ability of Personnels')),
                ('contractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ahp_app.Contractor')),
            ],
        ),
        migrations.AddField(
            model_name='bid',
            name='positive_response',
            field=models.CharField(blank=True, choices=[('1,1,1', 'Equally Preferred'), ('1,2,3', 'Equally to Moderately Preferred'), ('2,3,4', 'Moderately Preferred'), ('3,4,5', 'Moderately to Strongly Preferred'), ('4,5,6', 'Strongly Preferred'), ('5,6,7', 'Strongly to Very Strongly Preferred'), ('6,7,8', 'Very Strongly Preferred'), ('7,8,9', 'Very Strongly to Extremely Preferred'), ('8,9,9', 'Extremely Preferred')], max_length=100, null=True, verbose_name='Postive Response'),
        ),
        migrations.AddField(
            model_name='bid',
            name='reverse_response',
            field=models.CharField(blank=True, choices=[('1,1,1', 'Equally Preferred'), ('0.3333,0.5,1', 'Equally to Moderately Preferred'), ('0.25,0.3333,0.5', 'Moderately Preferred'), ('0.2, 0.25, 0.3333', 'Moderately to Strongly Preferred'), ('0.1667, 0.2, 0.25', 'Strongly Preferred'), ('0.1429, 0.1667, 0.2', 'Strongly to Very Strongly Preferred'), ('0.125, 0.1429, 0.1667', 'Very Strongly Preferred'), ('0.1111, 0.125, 0.1429', 'Very Strongly to Extremely Preferred'), ('0.1111, 0.1111, 0.125', 'Extremely Preferred')], max_length=100, null=True, verbose_name='Reverse Response'),
        ),
    ]
