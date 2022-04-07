# Generated by Django 4.0.3 on 2022-04-07 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('used', models.BooleanField(default=False)),
                ('image', models.CharField(default='', max_length=512)),
                ('name', models.CharField(default='', max_length=128)),
                ('description', models.CharField(default='', max_length=256)),
                ('price', models.FloatField(default=0)),
                ('price_before', models.IntegerField(default=0)),
                ('price_after', models.IntegerField(default=0)),
            ],
        ),
    ]