# Generated by Django 4.2.4 on 2023-08-04 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0006_alter_shorturl_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 3, 17, 35, 4, 761547)),
        ),
    ]
