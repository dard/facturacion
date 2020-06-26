# Generated by Django 3.0.7 on 2020-06-25 20:40

import builtins
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'ordering': [builtins.id],
            },
        ),
        migrations.AlterField(
            model_name='employed',
            name='date_sorted',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro'),
        ),
        migrations.AddField(
            model_name='employed',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='erp.Type'),
        ),
    ]