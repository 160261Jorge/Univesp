# Generated by Django 2.2.1 on 2021-11-22 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20211118_2203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionario',
            old_name='dose',
            new_name='doze',
        ),
    ]
