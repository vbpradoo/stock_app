# Generated by Django 2.0.7 on 2018-07-26 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Almacenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=40)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ['apellidos'],
            },
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
            ],
            options={
                'get_latest_by': 'fecha',
            },
        ),
        migrations.CreateModel(
            name='Lotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=10, unique=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
                ('unidades', models.CharField(max_length=3)),
                ('stock', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('vendido', models.BooleanField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_created')),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_updated')),
                ('articulo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.Articulo')),
                ('entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Entrada')),
            ],
        ),
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('destino', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='destino', to='stock.Almacenes')),
                ('origen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='origen', to='stock.Almacenes')),
            ],
            options={
                'get_latest_by': 'fecha',
            },
        ),
        migrations.CreateModel(
            name='Proovedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=40)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ['apellidos'],
            },
        ),
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('cantidad', models.IntegerField()),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.Cliente')),
            ],
            options={
                'get_latest_by': 'fecha',
            },
        ),
        migrations.AddField(
            model_name='lotes',
            name='movimientos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Movimientos'),
        ),
        migrations.AddField(
            model_name='lotes',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lotes', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AddField(
            model_name='lotes',
            name='salida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Salida'),
        ),
        migrations.AddField(
            model_name='entrada',
            name='proovedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.Proovedor'),
        ),
    ]