# Generated by Django 3.2 on 2021-04-26 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0002_auto_20210426_1117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parameter',
            old_name='title',
            new_name='name',
        ),
    ]