# Generated by Django 3.0.4 on 2020-03-08 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.IntegerField()),
                ('hora_extra', models.IntegerField()),
                ('hora_extra_especial', models.IntegerField()),
                ('hora_dia_descanso', models.IntegerField()),
                ('hora_dia_feriado', models.IntegerField()),
                ('adelanto', models.DecimalField(decimal_places=2, max_digits=9)),
                ('dia_faltado', models.IntegerField()),
            ],
        ),
    ]