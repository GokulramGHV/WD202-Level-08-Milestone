# Generated by Django 4.0.1 on 2022-02-22 09:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_emailsettings_email_enable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailsettings',
            name='email_time',
            field=models.TimeField(default=datetime.datetime(2022, 2, 22, 9, 51, 45, 593338, tzinfo=utc)),
        ),
    ]
