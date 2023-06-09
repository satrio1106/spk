# Generated by Django 4.2.1 on 2023-05-29 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alternatif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Kriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('benefit', 'benefit'), ('cost', 'cost')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Penilaian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelengkapan_fitur', models.IntegerField(default=0)),
                ('kemudahan_penggunaan', models.IntegerField(default=0)),
                ('keamanan', models.IntegerField(default=0)),
                ('biaya', models.IntegerField(default=0)),
                ('alternatif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.alternatif')),
            ],
        ),
        migrations.CreateModel(
            name='BobotNormalKriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bobot', models.FloatField(default=0)),
                ('kriteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.kriteria')),
            ],
        ),
        migrations.CreateModel(
            name='BobotKriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bobot', models.IntegerField(default=0)),
                ('kriteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.kriteria')),
            ],
        ),
    ]
