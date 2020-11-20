# Generated by Django 3.1 on 2020-08-24 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('previouscompany', models.EmailField(max_length=50, null=True)),
                ('noticeperiod', models.EmailField(max_length=50, null=True)),
                ('datecreated', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interviewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('sapid', models.EmailField(max_length=8, null=True)),
                ('datecreated', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Selected', 'Selected'), ('Rejected', 'Rejected')], max_length=50, null=True)),
                ('interviewdate', models.DateField(null=True)),
                ('interviewtime', models.TimeField(null=True)),
                ('remarks', models.CharField(max_length=50, null=True)),
                ('candidate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='interview.candidate')),
                ('ipanel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='interview.interviewer')),
            ],
        ),
    ]
