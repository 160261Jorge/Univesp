# Generated by Django 4.0.4 on 2022-07-02 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_paciente_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]