# Generated by Django 4.2.2 on 2023-06-21 15:06

import apps.users.managers
from django.db import migrations, models
import django.utils.timezone


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
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('gender', models.CharField(choices=[('мужчина', 'Мужчина'), ('женщина', 'Женщина'), ('другое', 'Другое')], default='другое', max_length=50, verbose_name='Пол')),
                ('position', models.CharField(choices=[('пользователь', 'Пользователь'), ('мастер', 'Мастер'), ('владелец', 'Владелец')], default='пользователь', max_length=50, verbose_name='Позиция')),
                ('created_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания юзера')),
                ('updated_dt', models.DateTimeField(auto_now=True, verbose_name='Последние обновление объекта')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', apps.users.managers.UserManager()),
            ],
        ),
    ]
