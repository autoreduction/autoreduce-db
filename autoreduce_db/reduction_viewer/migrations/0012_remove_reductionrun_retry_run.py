# Generated by Django 3.2.4 on 2021-10-18 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reduction_viewer', '0011_move_arguments_into_reductionarguments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reductionrun',
            name='retry_run',
        ),
    ]