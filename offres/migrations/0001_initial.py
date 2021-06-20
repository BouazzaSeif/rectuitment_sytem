# Generated by Django 3.2.3 on 2021-05-23 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('nb_poste', models.IntegerField(default=1)),
                ('entreprise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entreprise', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Condidature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('etat', models.IntegerField()),
                ('offre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='condidatures', to='offres.offre')),
            ],
        ),
    ]