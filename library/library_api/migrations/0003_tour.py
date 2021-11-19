# Generated by Django 3.2.8 on 2021-11-05 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_api', '0002_zone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=145)),
                ('slug', models.CharField(blank=True, max_length=45, null=True)),
                ('operador', models.CharField(blank=True, max_length=45, null=True)),
                ('tipoDeTour', models.CharField(blank=True, max_length=45, null=True)),
                ('descripcion', models.CharField(max_length=256)),
                ('img', models.CharField(blank=True, max_length=256, null=True)),
                ('pais', models.CharField(blank=True, max_length=45, null=True)),
                ('zonaLlegada', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tours_llegada', to='library_api.zone')),
                ('zonaSalida', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tours_salida', to='library_api.zone')),
            ],
        ),
    ]
