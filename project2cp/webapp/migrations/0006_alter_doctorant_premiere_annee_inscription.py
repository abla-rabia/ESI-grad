# Generated by Django 4.1.7 on 2023-03-31 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_rename_cs_pv_fichier_encadrant_laboratoire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorant',
            name='premiere_annee_inscription',
            field=models.DateField(max_length=100, null=True),
        ),
    ]