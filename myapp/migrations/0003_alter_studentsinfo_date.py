# Generated by Django 4.2.2 on 2023-09-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_studentsinfo_aadhaar_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsinfo',
            name='Date',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
