# Generated by Django 3.1.7 on 2021-03-20 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diabetes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pregnancies', models.CharField(max_length=20)),
                ('glucose', models.CharField(max_length=20)),
                ('blood_pressure', models.CharField(max_length=20)),
                ('skin_thickness', models.CharField(max_length=20)),
                ('insulin', models.CharField(max_length=20)),
                ('bmi', models.CharField(max_length=20)),
                ('diabetes_pedigree_function', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20)),
            ],
        ),
    ]
