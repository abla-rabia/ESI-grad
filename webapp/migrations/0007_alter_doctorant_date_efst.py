# Generated by Django 4.1.7 on 2023-04-18 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_doctorant_statut_alter_doctorant_sexe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorant',
            name='date_EFST',
            field=models.CharField(max_length=100, null=True),
        ),
    ]