# Generated by Django 4.0.4 on 2022-04-16 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0007_remove_vacancy_graduate_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancy',
            old_name='addressEssentional_duties_responsibilities',
            new_name='Essentional_duties_responsibilities',
        ),
    ]