# Generated by Django 4.0.4 on 2022-09-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_habitat_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitat',
            name='prix',
            field=models.DecimalField(decimal_places=2, default=1500000, max_digits=100000),
        ),
    ]