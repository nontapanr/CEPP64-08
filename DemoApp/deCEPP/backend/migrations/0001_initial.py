# Generated by Django 4.0.4 on 2022-05-08 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('StudentID', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('SubjectID', models.CharField(max_length=500)),
                ('Grade', models.CharField(max_length=2)),
                ('Semester', models.CharField(max_length=1)),
                ('Year', models.CharField(max_length=4)),
                ('Curriculum', models.CharField(max_length=500)),
            ],
        ),
    ]
