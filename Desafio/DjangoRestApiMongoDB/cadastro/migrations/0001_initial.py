# Generated by Django 3.2.13 on 2022-05-05 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=70)),
                ('email', models.CharField(default='', max_length=200)),
                ('telefone', models.CharField(default='', max_length=70)),
                ('endereco', models.CharField(default='', max_length=200)),
                ('profissao', models.CharField(default='', max_length=50)),
                ('curriculo', models.ImageField(default='', upload_to='')),
            ],
        ),
    ]
