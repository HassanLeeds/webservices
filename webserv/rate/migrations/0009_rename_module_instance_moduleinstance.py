# Generated by Django 5.1.6 on 2025-03-15 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0008_rename_module_rating_module_instance_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Module_instance',
            new_name='ModuleInstance',
        ),
    ]
