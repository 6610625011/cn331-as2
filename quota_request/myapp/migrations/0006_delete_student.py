# Generated by Django 5.1.1 on 2024-10-05 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_course_subject_credit'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]