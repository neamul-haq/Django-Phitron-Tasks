# Generated by Django 5.0.4 on 2024-05-30 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_categories', '0002_remove_category_task'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='category',
            field=models.ManyToManyField(to='task_categories.category'),
        ),
    ]
