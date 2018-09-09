# Generated by Django 2.1rc1 on 2018-09-08 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('is_attending', models.NullBooleanField(default=None)),
                ('is_child', models.BooleanField(default=False)),
            ],
        ),
    ]
