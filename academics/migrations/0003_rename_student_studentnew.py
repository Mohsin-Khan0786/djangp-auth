# Generated by Django 5.2.4 on 2025-07-31 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_student_age'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='StudentNew',
        ),
    ]
