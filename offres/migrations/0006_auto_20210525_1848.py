# Generated by Django 3.2.3 on 2021-05-25 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offres', '0005_auto_20210525_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condidature',
            name='college_name',
            field=models.TextField(default='0'),
        ),
        migrations.AlterField(
            model_name='condidature',
            name='company_names',
            field=models.TextField(default='0'),
        ),
        migrations.AlterField(
            model_name='condidature',
            name='mobile_number',
            field=models.TextField(default='0'),
        ),
    ]
