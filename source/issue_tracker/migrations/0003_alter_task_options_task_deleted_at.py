# Generated by Django 4.1.7 on 2023-03-03 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0002_task_is_deleted'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='task',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True, verbose_name='Дата и время удаления'),
        ),
    ]
