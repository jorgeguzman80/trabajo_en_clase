# Generated by Django 4.1.7 on 2023-04-03 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_cars_amount_alter_cars_price_alter_cars_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='date_purchase',
        ),
        migrations.AlterField(
            model_name='cars',
            name='state',
            field=models.CharField(choices=[('Comprado', 'Comprado'), ('Anulado', 'Anulado'), ('Activo', 'Activo')], default='activo', max_length=100),
        ),
    ]