# Generated by Django 3.2.9 on 2022-03-21 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0010_alter_student_detail_admission_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_detail',
            name='Admission_no',
            field=models.CharField(default='BRD/069807', max_length=10),
        ),
    ]