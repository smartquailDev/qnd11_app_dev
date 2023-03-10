# Generated by Django 3.2.16 on 2023-01-21 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0003_alter_service_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
        migrations.RemoveField(
            model_name='service',
            name='available',
        ),
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='comercial.category'),
        ),
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descripción'),
        ),
        migrations.AddField(
            model_name='service',
            name='name',
            field=models.CharField(choices=[('Limpieza complementaria', 'Limpieza complementaria'), ('Limpieza de vidrios', 'Limpieza de vidrios'), ('Limpieza de parqueaderos', 'Limpieza de parqueaderos'), ('Reciclado de residuos', 'Reciclado de residuos'), ('Venta de Insumos', 'Venta de Insumos')], db_index=True, max_length=200, null=True, verbose_name='Nombre de Servicio'),
        ),
        migrations.AddField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10000, null=True, verbose_name='Costo por punto'),
        ),
        migrations.AddField(
            model_name='service',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=100000, null=True, verbose_name='Costo base de servicio'),
        ),
    ]
