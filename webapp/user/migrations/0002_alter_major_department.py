# Generated by Django 4.1.2 on 2022-11-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='department',
            field=models.CharField(max_length=30, null=True, verbose_name='학부'),
        ),
    ]
