# Generated by Django 3.2.6 on 2021-08-03 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Tasa', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Monto', models.PositiveIntegerField()),
            ],
        ),
    ]
