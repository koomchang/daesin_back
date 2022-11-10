# Generated by Django 4.1.2 on 2022-11-09 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='제목')),
                ('content', models.TextField(max_length=2000, verbose_name='내용')),
                ('type', models.CharField(choices=[('REVIEW', 'review'), ('CLUBPOST', 'clubpost'), ('ADVERTISEMENT', 'advertisement')], max_length=20, null=True, verbose_name='글 종류')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정 일시')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'db_table': 'posts',
            },
        ),
    ]
