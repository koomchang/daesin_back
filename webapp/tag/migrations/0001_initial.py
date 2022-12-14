# Generated by Django 4.1.3 on 2022-11-29 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('club', '0001_initial'),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100, unique=True, verbose_name='태그')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='tag.tag', verbose_name='상위태그')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_tags', to='post.post')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_tags', to='tag.tag')),
            ],
            options={
                'verbose_name': 'PostTag',
                'verbose_name_plural': 'PostTags',
                'db_table': 'post_tags',
            },
        ),
        migrations.CreateModel(
            name='ClubTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club_tags', to='club.club')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club_tags', to='tag.tag')),
            ],
            options={
                'verbose_name': 'ClubTag',
                'verbose_name_plural': 'ClubTags',
                'db_table': 'club_tags',
            },
        ),
    ]