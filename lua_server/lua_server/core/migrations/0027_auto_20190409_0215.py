# Generated by Django 2.1.7 on 2019-04-09 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20190408_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_number',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]