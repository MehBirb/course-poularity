# Generated by Django 4.1.3 on 2022-12-07 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_number',
            new_name='course_population',
        ),
    ]
