# Generated by Django 3.1.7 on 2021-03-23 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('character_sheet', '0006_auto_20210323_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='damage',
            name='name',
        ),
    ]
