# Generated by Django 2.1rc1 on 2018-09-23 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0009_auto_20180923_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='is_attending',
            field=models.BooleanField(choices=[(True, 'Will Attend'), (False, 'Will Not Attend')]),
        ),
    ]