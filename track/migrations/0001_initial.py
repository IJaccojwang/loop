# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-30 08:06
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
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=255)),
                ('business_email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighbourhood_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('occupants', models.IntegerField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilepic', models.ImageField(upload_to='profiles/')),
                ('bio', models.CharField(max_length=255)),
                ('neighbourhood_id', models.CharField(max_length=255)),
                ('profile_email', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='neighbourhood_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='track.Neighbourhood'),
        ),
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
