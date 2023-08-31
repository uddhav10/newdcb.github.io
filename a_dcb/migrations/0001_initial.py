# Generated by Django 4.1.3 on 2022-11-25 09:41

import a_dcb.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to=a_dcb.models.path_and_rename)),
                ('complaint', models.CharField(max_length=5000)),
            ],
        ),
    ]
