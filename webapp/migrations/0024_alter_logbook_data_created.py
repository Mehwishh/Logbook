# Generated by Django 4.2.4 on 2023-08-23 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0023_alter_logbook_data_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logbook',
            name='data_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
