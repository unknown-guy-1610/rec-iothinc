# Generated by Django 2.0.12 on 2019-12-09 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('q_id', models.IntegerField()),
                ('question', models.CharField(max_length=1000)),
                ('o1', models.CharField(max_length=200)),
                ('o2', models.CharField(max_length=200)),
                ('o3', models.CharField(max_length=200)),
                ('o4', models.CharField(max_length=200)),
                ('co', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='SN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('register_number', models.CharField(blank=True, default='', max_length=100)),
                ('email_id', models.CharField(max_length=253)),
                ('phone', models.CharField(max_length=253)),
                ('tech', models.BooleanField(default=False)),
                ('mgt', models.BooleanField(default=False)),
                ('design', models.BooleanField(default=False)),
                ('otp', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
