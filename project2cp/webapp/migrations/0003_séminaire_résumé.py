# Generated by Django 4.1.7 on 2023-03-14 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_doctorant_sexe'),
    ]

    operations = [
        migrations.AddField(
            model_name='séminaire',
            name='résumé',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
