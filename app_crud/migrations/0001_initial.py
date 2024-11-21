# Generated by Django 5.1.3 on 2024-11-21 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('numero_patrimonio', models.CharField(max_length=50, unique=True)),
                ('data_aquisicao', models.DateField()),
                ('status', models.CharField(choices=[('disponível', 'Disponível'), ('em uso', 'Em uso'), ('em manutenção', 'Em manutenção'), ('descartado', 'Descartado')], default='disponível', max_length=20)),
            ],
        ),
    ]
