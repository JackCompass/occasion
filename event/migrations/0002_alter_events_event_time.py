# Generated by Django 3.2.6 on 2021-08-27 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_time',
            field=models.DateField(),
        ),
    ]
