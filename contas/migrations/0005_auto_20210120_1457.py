# Generated by Django 3.1.5 on 2021-01-20 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0004_auto_20210120_1408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transacoes',
            old_name='dt_criação',
            new_name='data',
        ),
    ]