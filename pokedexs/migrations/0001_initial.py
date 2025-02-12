# Generated by Django 2.2.4 on 2019-12-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('pokemon_number', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('pokemon_name', models.CharField(max_length=30, unique=True)),
                ('attack', models.SmallIntegerField()),
                ('classfication', models.CharField(max_length=100)),
                ('defense', models.SmallIntegerField()),
                ('height_m', models.CharField(blank=True, max_length=10, null=True)),
                ('hp', models.SmallIntegerField()),
                ('speed', models.SmallIntegerField()),
                ('type1', models.CharField(max_length=15)),
                ('type2', models.CharField(max_length=15)),
                ('weight_kg', models.CharField(max_length=10)),
                ('generation', models.IntegerField()),
                ('is_legendary', models.IntegerField()),
                ('abilities', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'pokemon',
                'managed': False,
            },
        ),
    ]
