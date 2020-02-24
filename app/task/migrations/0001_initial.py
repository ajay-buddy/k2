# Generated by Django 2.1.15 on 2020-02-24 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
        ('spaces', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('task_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_created_by', to=settings.AUTH_USER_MODEL)),
                ('project_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_belongs_to_space', to='project.Project')),
                ('space_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_belongs_to_space', to='spaces.Space')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
