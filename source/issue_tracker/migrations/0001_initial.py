# Generated by Django 4.1.7 on 2023-03-03 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=100, verbose_name='Краткое описание')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Полное описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время и дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время и дата обновления')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='statuses', to='issue_tracker.status', verbose_name='Статус')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='issue_tracker.type', verbose_name='Тип')),
            ],
        ),
    ]
