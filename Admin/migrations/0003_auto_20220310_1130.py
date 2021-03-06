# Generated by Django 3.2.9 on 2022-03-10 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_fileupload_lecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Duration',
            field=models.CharField(choices=[('6 mon', '6 MONTH'), ('1 mon', '1 MONTH'), ('3 mon', '3 MONTH')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='Thumb',
            field=models.ImageField(null=True, upload_to='static/Admin/img'),
        ),
    ]
