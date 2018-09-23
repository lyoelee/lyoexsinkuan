# Generated by Django 2.1rc1 on 2018-09-23 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0007_auto_20180923_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='whatsapp_phone_number',
        ),
        migrations.AddField(
            model_name='guest',
            name='name',
            field=models.CharField(default=False, max_length=50),
        ),
        migrations.AddField(
            model_name='guest',
            name='whatsapp_number',
            field=models.CharField(default=False, max_length=13),
        ),
    ]