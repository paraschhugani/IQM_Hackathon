# Generated by Django 4.0.6 on 2022-11-13 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Janta', '0008_alter_complaint_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='email',
            field=models.EmailField(default='default@email.com', max_length=100, null=True),
        ),
    ]
