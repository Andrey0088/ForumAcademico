# Generated by Django 5.0.2 on 2024-03-18 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0011_disciplina_remove_post_foto_perfil_post_disciplinas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='descricao',
        ),
    ]
