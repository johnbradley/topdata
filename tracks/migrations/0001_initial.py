# Generated by Django 2.2.3 on 2020-03-11 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CellType',
            fields=[
                ('name', models.CharField(help_text='Name of the cell type', max_length=255, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genome',
            fields=[
                ('name', models.CharField(help_text='Name of the genome', max_length=255, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RepName',
            fields=[
                ('name', models.CharField(help_text='Replicate name', max_length=255, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TranscriptionFactor',
            fields=[
                ('name', models.CharField(help_text='Name of the transcription factor', max_length=255, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the track', max_length=255)),
                ('short_label', models.CharField(help_text='Short label used in trackDb.txt', max_length=255)),
                ('long_label', models.CharField(help_text='Long label used in trackDb.txt', max_length=255)),
                ('big_data_url', models.URLField(help_text='URL used for bigDataUrl in trackDb.txt', max_length=1000)),
                ('file_type', models.CharField(help_text='Type of file referenced by big_data_url', max_length=255)),
                ('position', models.CharField(help_text='Genome Browser position value', max_length=255)),
                ('cell_type', models.ForeignKey(help_text='Cell type', on_delete=django.db.models.deletion.CASCADE, to='tracks.CellType')),
                ('genome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracks.Genome')),
                ('rep_name', models.ForeignKey(help_text='Replicate name', on_delete=django.db.models.deletion.CASCADE, to='tracks.RepName')),
                ('tf', models.ForeignKey(help_text='Transcription factor', on_delete=django.db.models.deletion.CASCADE, to='tracks.TranscriptionFactor')),
            ],
            options={
                'unique_together': {('genome', 'name')},
            },
        ),
    ]
