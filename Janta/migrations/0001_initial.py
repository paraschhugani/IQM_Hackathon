# Generated by Django 4.0.6 on 2022-11-12 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('Uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('severity', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='0', max_length=1)),
                ('department', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='complaint/proofs')),
                ('location', models.CharField(max_length=100)),
                ('send_to_email', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('1', 'Submitted'), ('2', 'Verified'), ('3', 'Assigned'), ('4', 'Processing'), ('5', 'Resolved')], default='1', max_length=1)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]