# Generated by Django 4.0.1 on 2022-02-20 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_emailsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailsettings',
            name='email_enable',
            field=models.BooleanField(default=True),
        ),
    ]