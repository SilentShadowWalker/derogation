# Generated by Django 5.1 on 2024-09-24 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('city', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'wilaya',
                'managed': False,
            },
        ),
    ]
