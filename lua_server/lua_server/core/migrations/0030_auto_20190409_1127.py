# Generated by Django 2.1.7 on 2019-04-09 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20190409_0235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plan',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='planner',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='planners', to=settings.AUTH_USER_MODEL),
        ),
    ]