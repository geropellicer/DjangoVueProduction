# Generated by Django 2.1.7 on 2019-08-29 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canchas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alquiler',
            options={'verbose_name_plural': 'alquileres'},
        ),
        migrations.AlterModelOptions(
            name='cancha',
            options={'verbose_name_plural': 'canchas'},
        ),
        migrations.AlterField(
            model_name='cancha',
            name='tipo',
            field=models.CharField(choices=[('Cancha de 11', '11'), ('7ABIERTA', 'Cancha de 7 abierta'), ('5ABIERTA', 'Cancha de 5 abierta'), ('7TECHADA', 'Cancha de 7 techada'), ('5TECHADA', 'Cancha de 5 techada')], default='Cancha de 5 techada', max_length=20),
        ),
    ]
