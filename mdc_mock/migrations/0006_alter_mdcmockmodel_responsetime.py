# Generated by Django 4.1.3 on 2023-02-03 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdc_mock', '0005_alter_mdcmockmodel_requesturl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mdcmockmodel',
            name='responseTime',
            field=models.IntegerField(default=4, verbose_name='响应时间'),
        ),
    ]
