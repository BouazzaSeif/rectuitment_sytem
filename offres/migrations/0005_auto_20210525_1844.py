# Generated by Django 3.2.3 on 2021-05-25 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offres', '0004_auto_20210525_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='condidature',
            name='college_name',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='condidature',
            name='company_names',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='condidature',
            name='degree',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='condidature',
            name='designation',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='condidature',
            name='skills',
            field=models.TextField(default='0'),
        ),
        migrations.AddField(
            model_name='condidature',
            name='total_experience',
            field=models.IntegerField(default=0),
        ),
    ]