# Generated by Django 2.0 on 2019-04-08 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0011_category_cutoff'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='depart',
            field=models.CharField(default='Mechanical', max_length=20),
        ),
    ]
