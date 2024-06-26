# Generated by Django 4.2.1 on 2023-05-16 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_alter_doctorant_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='pv',
            name='année',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='co_directeur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='co_dir', to='webapp.encadrant'),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='observation',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
