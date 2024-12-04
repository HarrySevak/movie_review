# Generated by Django 4.0.4 on 2024-12-02 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('year', models.PositiveSmallIntegerField()),
                ('actors', models.CharField(max_length=200)),
                ('review', models.TextField()),
                ('stars', models.CharField(choices=[('s', 1), ('ss', 2), ('sss', 3), ('ssss', 4)], default=1, max_length=4)),
            ],
        ),
    ]
