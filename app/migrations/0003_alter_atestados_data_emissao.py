# Generated by Django 3.2.3 on 2021-05-21 15:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_atestados_numero_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atestados',
            name='data_emissao',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
