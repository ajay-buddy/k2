# Generated by Django 2.2 on 2021-05-03 22:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientBinding',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('client', models.UUIDField(default=uuid.uuid4)),
                ('study_group', models.UUIDField(default=uuid.uuid4)),
            ],
        ),
    ]
