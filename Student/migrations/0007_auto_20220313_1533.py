# Generated by Django 3.2.9 on 2022-03-13 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0006_auto_20220313_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_detail',
            name='doc_10',
            field=models.FileField(null=True, upload_to='static/docs/'),
        ),
        migrations.AlterField(
            model_name='student_detail',
            name='doc_12',
            field=models.FileField(null=True, upload_to='static/docs/'),
        ),
        migrations.AlterField(
            model_name='student_detail',
            name='doc_pg',
            field=models.FileField(null=True, upload_to='static/docs/'),
        ),
        migrations.AlterField(
            model_name='student_detail',
            name='doc_ug',
            field=models.FileField(null=True, upload_to='static/docs/'),
        ),
    ]
