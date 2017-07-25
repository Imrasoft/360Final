# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-24 06:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=6)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('year_of_first_medical_certification', models.CharField(max_length=4)),
                ('mobile_number', models.CharField(blank=True, max_length=30, null=True)),
                ('about_me', models.TextField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('hospital', models.CharField(blank=True, max_length=30, null=True)),
                ('work_number', models.CharField(blank=True, max_length=30, null=True)),
                ('avatar', models.ImageField(blank=True, default='avatars/none/default.jpeg', null=True, upload_to='avatars')),
                ('website', models.URLField(blank=True, null=True)),
                ('verification_status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('other_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('sex', models.CharField(max_length=1)),
                ('employer', models.CharField(max_length=100)),
                ('postal_address', models.CharField(max_length=100)),
                ('first_registration', models.CharField(max_length=100)),
                ('date_of_first_registration', models.CharField(max_length=100)),
                ('additional_qualifications', models.TextField()),
                ('speciality', models.CharField(max_length=100)),
                ('receipt_number', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='records')),
                ('synced', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_site', models.CharField(choices=[('LinkedIn', 'LinkedIn'), ('Facebook', 'Facebook'), ('Twitter', 'Twitter'), ('Youtube', 'Youtube')], max_length=50)),
                ('username', models.CharField(max_length=100)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.Profession'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.Specialization'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]