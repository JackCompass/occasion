# Generated by Django 3.2.6 on 2021-08-27 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, default='images/defaultEvent.png', null=True, upload_to='images/')),
                ('location', models.CharField(max_length=50)),
                ('event_time', models.TimeField()),
            ],
        ),
    ]
