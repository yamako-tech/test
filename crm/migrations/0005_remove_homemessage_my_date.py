# Generated by Django 4.1 on 2022-08-29 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_homemessage_my_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homemessage',
            name='my_date',
        ),
    ]
