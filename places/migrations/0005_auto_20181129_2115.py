# Generated by Django 2.1.3 on 2018-11-30 03:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('places', '0004_auto_20181129_2005'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Eval_place',
            new_name='EvalPlace',
        ),
    ]
