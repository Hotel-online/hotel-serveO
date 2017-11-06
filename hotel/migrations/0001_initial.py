from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('fotos', models.ImageField(blank=True, upload_to='')),
                ('precio', models.FloatField(default=0.0)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=11)),
                ('tipoCliente', models.CharField(max_length=11)),
                ('informacionAdicional', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Person')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='DetalleReservacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'DetalleReservacion',
                'verbose_name_plural': 'DetalleReservaciones',
            },
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'DetalleVenta',
                'verbose_name_plural': 'DetalleVentas',
            },
        ),
        migrations.CreateModel(
            name='Doc_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documento', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Doc_Type',
                'verbose_name_plural': 'Doc_Types',
            },
        ),
        migrations.CreateModel(
            name='Forma_de_pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formaPago', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Forma_de_pago',
                'verbose_name_plural': 'Forma_de_pagos',
            },
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amueblado', models.CharField(max_length=10)),
                ('codigo', models.CharField(max_length=10)),
                ('estado', models.CharField(max_length=1)),
                ('categoriaHabitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Categoria')),
            ],
            options={
                'verbose_name': 'Habitacion',
                'verbose_name_plural': 'Habitaciones',
            },
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_doc_referencia', models.CharField(max_length=15)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('total', models.FloatField(default=0)),
                ('forma_de_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Forma_de_pago')),
            ],
            options={
                'verbose_name': 'Reservacion',
                'verbose_name_plural': 'Reservaciones',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_doc', models.CharField(max_length=15)),
                ('numeroReservacion', models.IntegerField()),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.Cliente')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='doc_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Doc_Type'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Venta'),
        ),
        migrations.AddField(
            model_name='detallereservacion',
            name='habitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Habitacion'),
        ),
    ]
