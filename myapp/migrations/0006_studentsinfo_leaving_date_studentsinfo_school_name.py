# Generated by Django 4.2.2 on 2023-09-14 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_studentsinfo_student_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsinfo',
            name='Leaving_date',
            field=models.CharField(default='Not Available', max_length=30),
        ),
        migrations.AddField(
            model_name='studentsinfo',
            name='School_name',
            field=models.CharField(default='Not Available', max_length=100),
        ),
    ]
