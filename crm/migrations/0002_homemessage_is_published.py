# Generated by Django 4.1 on 2022-08-25 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homemessage',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Published'),
        ),
    ]
