# Generated by Django 4.1.7 on 2023-04-29 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_pv_ordre_du_jour_alter_doctorant_option_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctorant',
            old_name='a_soutenue',
            new_name='soutenu',
        ),
        migrations.RemoveField(
            model_name='doctorant',
            name='abondant',
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='date_EFST',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='sexe',
            field=models.CharField(choices=[('Masculin', 'Masculin'), ('Féminin', 'Féminin')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='statut',
            field=models.CharField(choices=[('Inscrit', 'Inscrit'), ('Soutenu', 'Soutenu'), ('Différé', 'Différé'), ('Radié', 'Radié')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='tab_séminaires',
            field=models.ManyToManyField(blank=True, to='webapp.séminaire'),
        ),
    ]