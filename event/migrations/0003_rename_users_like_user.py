# Generated by Django 3.2.6 on 2021-08-27 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20210827_1736'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='users',
            new_name='user',
        ),
    ]
