# Generated by Django 4.0.6 on 2022-11-12 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Department', '0001_initial'),
        ('Janta', '0002_complaint_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Department.department_user'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Department.department'),
        ),
    ]