# Generated by Django 3.2.9 on 2022-03-24 18:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Student', '0017_auto_20220323_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date2',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student_detail',
            name='Admission_no',
            field=models.CharField(default='BRD/954461', max_length=10),
        ),
    ]
