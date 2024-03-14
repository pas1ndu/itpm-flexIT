# Generated by Django 4.0.4 on 2022-04-15 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('company_type', models.CharField(max_length=200, null=True)),
                ('job_title', models.CharField(max_length=200, null=True)),
                ('graduate_status', models.CharField(max_length=200, null=True)),
                ('working_status', models.CharField(max_length=200, null=True)),
                ('working_hours', models.CharField(max_length=200, null=True)),
                ('no_of_applicants', models.CharField(max_length=200, null=True)),
                ('experience', models.CharField(max_length=200, null=True)),
                ('job_roll', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
