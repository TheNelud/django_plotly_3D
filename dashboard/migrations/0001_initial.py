# Generated by Django 4.0.5 on 2022-06-07 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skv_name', models.CharField(max_length=100)),
                ('skv_x', models.FloatField()),
                ('skv_y', models.FloatField()),
                ('skv_z', models.FloatField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
