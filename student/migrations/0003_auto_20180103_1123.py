# Generated by Django 2.0.1 on 2018-01-03 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20180103_0909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='createby',
            new_name='createdby',
        ),
    ]
