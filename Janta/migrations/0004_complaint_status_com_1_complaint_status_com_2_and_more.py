# Generated by Django 4.0.6 on 2022-11-12 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Janta', '0003_complaint_assigned_to_alter_complaint_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='status_com_1',
            field=models.CharField(default='Complaint Submitted', max_length=1000),
        ),
        migrations.AddField(
            model_name='complaint',
            name='status_com_2',
            field=models.CharField(default='Complaint Verified', max_length=1000),
        ),
        migrations.AddField(
            model_name='complaint',
            name='status_com_3',
            field=models.CharField(default='Complaint Assigned', max_length=1000),
        ),
        migrations.AddField(
            model_name='complaint',
            name='status_com_4',
            field=models.CharField(default='Complaint Processing', max_length=1000),
        ),
        migrations.AddField(
            model_name='complaint',
            name='status_com_5',
            field=models.CharField(default='Complaint Resolved', max_length=1000),
        ),
    ]