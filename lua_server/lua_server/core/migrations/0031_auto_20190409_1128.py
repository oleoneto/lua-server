# Generated by Django 2.1.7 on 2019-04-09 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20190409_1127'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Plan',
            new_name='StudyPlan',
        ),
    ]