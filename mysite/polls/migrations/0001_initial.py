# Generated by Django 3.2.4 on 2021-06-16 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('info', models.CharField(max_length=20)),
            ],
        ),
    ]
