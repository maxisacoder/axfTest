# Generated by Django 3.2.5 on 2021-07-26 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0003_nav'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mustbuy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=20)),
                ('trackid', models.CharField(max_length=20)),
            ],
        ),
    ]