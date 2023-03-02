# Generated by Django 3.2.9 on 2022-03-21 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0013_alter_student_detail_admission_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_payment',
            name='Admission_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Student.student_detail'),
        ),
        migrations.AlterField(
            model_name='student_detail',
            name='Admission_no',
            field=models.CharField(default='BRD/312235', max_length=10),
        ),
    ]
