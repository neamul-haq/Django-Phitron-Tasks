# Generated by Django 5.0.4 on 2024-05-26 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_modelform_father_name_alter_modelform_roll'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelform',
            name='mother_name',
            field=models.TextField(default='Rahima'),
        ),
        migrations.AlterField(
            model_name='modelform',
            name='father_name',
            field=models.TextField(default='Rahim'),
        ),
    ]