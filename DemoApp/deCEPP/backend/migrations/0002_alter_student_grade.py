# Generated by Django 4.0.4 on 2022-05-08 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Grade',
            field=models.CharField(default='ไม่มีข้อมูล', max_length=2),
        ),
    ]
