# Generated by Django 4.0.3 on 2022-03-20 17:23

from django.db import migrations, models



class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('place', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('text', models.CharField(max_length=250)),
                ('color', models.CharField(max_length=10)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('deadline', models.DateTimeField()),
                ('done', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('title', models.CharField(max_length=250)),
            ],
        ),

        migrations.CreateModel(
            name='Login',
            fields=[
                ('title', models.CharField(max_length=250)),
            ],
        ),
    ]



