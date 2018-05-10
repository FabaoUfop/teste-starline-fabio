# Generated by Django 2.0.5 on 2018-05-10 03:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('questao_id', models.AutoField(primary_key=True, serialize=False)),
                ('questao_area', models.CharField(choices=[('M', 'Medicas'), ('H', 'Humanas'), ('E', 'Exatas'), ('G', 'Gerenciais')], max_length=1)),
                ('questao_disciplina', models.CharField(max_length=40)),
                ('questao_pergunta', models.TextField(max_length=100)),
                ('questao_tipo', models.CharField(choices=[('O', 'Objetiva'), ('D', 'Discursiva')], max_length=1)),
                ('questao_objetiva', models.CharField(blank=True, choices=[('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd')], max_length=1, null=True)),
                ('questao_discursiva', models.TextField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Questao',
                'ordering': ['questao_pergunta'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_nome', models.CharField(max_length=255)),
                ('user_email', models.EmailField(max_length=75)),
            ],
        ),
        migrations.AddField(
            model_name='questao',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
