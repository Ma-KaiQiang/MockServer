# Generated by Django 4.1.3 on 2023-02-09 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0005_alter_user_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='sex',
        ),
    ]
