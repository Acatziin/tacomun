# Generated by Django 2.1.3 on 2018-11-28 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_name',
            field=models.CharField(max_length=45, unique=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='postal_code',
            field=models.IntegerField(),
        ),
    ]
