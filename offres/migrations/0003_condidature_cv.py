# Generated by Django 3.2.3 on 2021-05-25 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offres', '0002_alter_condidature_etat'),
    ]

    operations = [
        migrations.AddField(
            model_name='condidature',
            name='CV',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
