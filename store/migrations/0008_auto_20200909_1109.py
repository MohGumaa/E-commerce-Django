# Generated by Django 3.1.1 on 2020-09-09 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20200909_1053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orderd',
            new_name='ordered',
        ),
    ]
