# Generated by Django 2.1.7 on 2019-04-27 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_caderneta'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['day', 'start_time', 'title']},
        ),
        migrations.AlterField(
            model_name='student',
            name='plans',
            field=models.ManyToManyField(blank=True, help_text='Individual study plans for student', to='core.StudyPlan'),
        ),
    ]
