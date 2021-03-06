# Generated by Django 3.2.8 on 2022-04-13 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_ctvarchive_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoneBrothArchive',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=25)),
                ('count', models.IntegerField()),
                ('date', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DeepArchive',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=25)),
                ('count', models.IntegerField()),
                ('date', models.IntegerField()),
            ],
        ),
    ]
