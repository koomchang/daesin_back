# Generated by Django 4.1.3 on 2022-12-03 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0004_alter_advertisement_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'ordering': ['-end_date'], 'verbose_name': 'Advertisement', 'verbose_name_plural': 'Advertisements'},
        ),
    ]