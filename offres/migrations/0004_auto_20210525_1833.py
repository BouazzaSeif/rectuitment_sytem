# Generated by Django 3.2.3 on 2021-05-25 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offres', '0003_condidature_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='condidature',
            name='mobile_number',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AlterField(
            model_name='condidature',
            name='CV',
            field=models.FileField(default=1, upload_to='CvExtractor'),
            preserve_default=False,
        ),
    ]