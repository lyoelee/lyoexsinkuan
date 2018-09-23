# Generated by Django 2.1rc1 on 2018-09-23 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0004_auto_20180923_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='comments',
            field=models.TextField(default=False),
        ),
        migrations.AlterField(
            model_name='guest',
            name='is_attending',
            field=models.BooleanField(choices=[(True, 'Will Attend'), (False, 'Will Not Attend')], default=False),
        ),
    ]