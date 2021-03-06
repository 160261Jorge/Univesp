# Generated by Django 2.2.1 on 2021-11-19 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20211116_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario',
            name='cinco',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='Seu filho já brincou de faz-de-conta, como, por exemplo, fazer de conta que está falando no telefone ou que está cuidando da boneca, ou qualquer outra brincadeira de faz-de-conta?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='desesseis',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='Seu filho já sabe andar?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='desessete',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='O seu filho olha para coisas que você está olhando?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='dez',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='O seu filho olha para você no olho por mais de um segundo ou dois?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='dezenove',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='O seu filho tenta sua atenção para a atividade dele?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='dezoito',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='O seu filho faz movimentos estranhos com os dedos perto do rosto dele?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='dois',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='Seu filho tem interesse por outras crianças?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='dose',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='O seu filho sorri em resposta ao seu rosto ou ao seu sorriso?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='nove',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='O seu filho alguma vez trouxe objetos para você (pais) para lhe mostrar este objeto?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='oito',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='Seu filho consegue brincar de forma correta com brinquedos pequenos (ex. carros ou blocos), sem apenas colocar na boca, remexer no brinquedo ou deixar o brinquedo cair?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='onze',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='O seu filho já pareceu muito sensível ao barulho (ex. tapando os ouvidos)?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='quatorze',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='O seu filho responde quando você chama ele pelo nome?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='quatro',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='Seu filho gosta de brincar de esconder e mostrar o rosto ou de esconde-esconde?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='quinze',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='Se você aponta um brinquedo do outro lado do cômodo, o seu filho olha para ele?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='seis',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='Seu filho já usou o dedo indicador dele para apontar, para pedir alguma coisa?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='sete',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='Seu filho já usou o dedo indicador dele para apontar, para indicar interesse em algo?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='tres',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='Seu filho gosta de subir em coisas, como escadas ou móveis?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='treze',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='O seu filho imita você? (ex. você faz expressões/caretas e seu filho imita)?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='um',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='Seu filho gosta de se balançar, de pular no seu joelho, etc?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='vinte',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='Você alguma vez já se perguntou se seu filho é surdo?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='vintedois',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='O seu filho às vezes fica aéreo, “olhando para o nada” ou caminhando sem direção definida?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='vintetres',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='O seu filho olha para o seu rosto para conferir a sua reação quando vê algo estranho?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='vinteum',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, null=True, verbose_name='O seu filho entende o que as pessoas dizem?'),
        ),
    ]
