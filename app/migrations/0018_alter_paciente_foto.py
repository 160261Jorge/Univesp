# Generated by Django 4.0.4 on 2022-05-30 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20220426_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='foto'),
        ),
    ]
