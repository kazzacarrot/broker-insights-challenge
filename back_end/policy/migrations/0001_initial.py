# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-05-27 14:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Insurer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premium', models.DecimalField(decimal_places=2, max_digits=7)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policy.Customer')),
                ('insurer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='policy.Insurer')),
            ],
        ),
        migrations.CreateModel(
            name='PolicyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='policy',
            name='policy_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policy.PolicyType'),
        ),
    ]
