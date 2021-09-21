# Generated by Django 3.2.7 on 2021-09-21 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('cost', models.IntegerField()),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]
