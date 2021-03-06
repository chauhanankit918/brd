# Generated by Django 3.2.9 on 2022-03-10 05:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, null=True)),
                ('Email', models.CharField(max_length=30, null=True)),
                ('Number', models.CharField(max_length=12, null=True)),
                ('Aadhaar', models.CharField(max_length=12, null=True)),
                ('Enrollment_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), (')', 'Other')], max_length=4, null=True)),
                ('Education', models.CharField(choices=[('10th', 'Secondary education'), ('12th', 'Senior secondary education'), ('Grad', 'Graduation education'), ('P.Grad', 'Post Graduation education')], max_length=50, null=True)),
                ('doc_10', models.FileField(null=True, upload_to='static/docs')),
                ('doc_12', models.FileField(null=True, upload_to='static/docs')),
                ('doc_ug', models.FileField(null=True, upload_to='static/docs')),
                ('doc_pg', models.FileField(null=True, upload_to='static/docs')),
                ('Address', models.TextField(max_length=200, null=True)),
                ('date_of_joining', models.DateField(default=datetime.datetime.today)),
                ('paid_amount', models.BigIntegerField(null=True)),
                ('Payment', models.BooleanField(default='False')),
                ('Trm', models.BooleanField(default='False')),
                ('Course_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.course')),
            ],
        ),
    ]
