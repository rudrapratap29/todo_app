# Generated by Django 4.2.2 on 2023-06-28 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_rename_created_task_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='complete',
            new_name='completed',
        ),
    ]
