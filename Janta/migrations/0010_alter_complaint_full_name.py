# Generated by Django 4.0.6 on 2022-11-13 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Janta', '0009_alter_complaint_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='full_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
