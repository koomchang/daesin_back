# Generated by Django 4.1.3 on 2022-11-24 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='division',
            name='major',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.major'),
        ),
        migrations.AddField(
            model_name='club',
            name='division',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='club.division', verbose_name='구분'),
        ),
    ]
