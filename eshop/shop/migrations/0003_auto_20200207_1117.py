# Generated by Django 3.0.3 on 2020-02-07 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200207_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='availiable',
            new_name='available',
        ),
    ]