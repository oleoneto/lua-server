# Generated by Django 2.1.7 on 2019-04-26 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190426_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='course',
        ),
        migrations.AddField(
            model_name='assignment',
            name='course_offer',
            field=models.ForeignKey(default=3390502031597, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assignments', to='core.CourseOffer'),
            preserve_default=False,
        ),
    ]
