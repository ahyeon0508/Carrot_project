# Generated by Django 2.2.14 on 2020-07-22 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20200722_1121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carrot_test',
            options={'ordering': ['time']},
        ),
    ]