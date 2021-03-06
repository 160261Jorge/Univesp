# Generated by Django 2.2.1 on 2021-11-10 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20211103_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='cpf',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='cpf'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='dn',
            field=models.DateField(blank=True, null=True, verbose_name='dn'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='prontuario',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Prontuario'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='desessete',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, verbose_name='desessete'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='dezoito',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, verbose_name='dezoito'),
        ),
    ]
