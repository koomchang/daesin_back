# Generated by Django 4.1.2 on 2022-11-10 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('nickname', models.CharField(max_length=20, null=True, unique=True)),
                ('grade', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(choices=[('LIB', '글로벌인문지역대학'), ('SOC', '사회과학대학'), ('LAW', '법과대학'), ('COM', '경상대학'), ('ENG', '창의공과대학'), ('DES', '조형대학'), ('NAT', '과학기술대학'), ('ART', '예술대학'), ('PHY', '체육대학'), ('BUS', '경영대학'), ('SOF', '소프트웨어융합대학'), ('ARC', '건축대학'), ('CAR', '자동차융합대학'), ('MOB', '미래모빌리티학과')], max_length=3, verbose_name='단과대')),
                ('department', models.CharField(max_length=30, verbose_name='학부')),
                ('sub_major', models.CharField(max_length=30, null=True, verbose_name='전공')),
            ],
            options={
                'verbose_name': 'Major',
                'verbose_name_plural': 'Majors',
                'db_table': 'majors',
            },
        ),
        migrations.CreateModel(
            name='UserMajor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1, verbose_name='전공순위')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_majors', to='user.major', verbose_name='학과')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_majors', to=settings.AUTH_USER_MODEL, verbose_name='유저')),
            ],
            options={
                'verbose_name': 'UserMajor',
                'verbose_name_plural': 'UserMajors',
                'db_table': 'usermajors',
            },
        ),
    ]
