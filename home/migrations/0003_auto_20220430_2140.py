# Generated by Django 3.1.4 on 2022-04-30 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_course_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_courses',
            new_name='courses',
        ),
    ]