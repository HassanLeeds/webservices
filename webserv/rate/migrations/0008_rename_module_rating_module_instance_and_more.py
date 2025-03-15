# Generated by Django 5.1.6 on 2025-03-14 02:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0007_alter_rating_professor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='module',
            new_name='module_instance',
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user', 'professor', 'module_instance')},
        ),
    ]
