# Generated by Django 3.0 on 2019-12-12 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gambar', models.CharField(max_length=200)),
                ('Nama', models.CharField(max_length=200)),
                ('Harga', models.CharField(max_length=200)),
            ],
        ),
    ]
