# Generated by Django 3.1 on 2020-09-26 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('documentoIdentidad', models.CharField(max_length=8)),
                ('nombres', models.CharField(max_length=20)),
                ('apellidoPaterno', models.CharField(max_length=20)),
                ('apellidoMaterno', models.CharField(max_length=20)),
                ('genero', models.CharField(max_length=10)),
                ('fechaNacimiento', models.DateField()),
                ('fechaCreacion', models.DateField()),
                ('estado', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.usuario')),
                ('preferencias', models.CharField(max_length=20)),
            ],
            bases=('main.usuario',),
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.usuario')),
                ('reputacion', models.FloatField()),
                ('coberturaEntrega', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.localizacion')),
            ],
            bases=('main.usuario',),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaCreacion', models.DateField()),
                ('estado', models.CharField(max_length=20)),
                ('fechaEntrega', models.DateField()),
                ('direccionEntrega', models.CharField(max_length=20)),
                ('tarifa', models.FloatField()),
                ('ubicacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.localizacion')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.cliente')),
                ('repartidor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.colaborador')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.FloatField()),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.pedido')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.producto')),
            ],
        ),
    ]
