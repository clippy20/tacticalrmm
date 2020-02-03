# Generated by Django 3.0.2 on 2020-02-03 04:04

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(default='0.1.0', max_length=255)),
                ('operating_system', models.CharField(max_length=255, null=True)),
                ('plat', models.CharField(max_length=255, null=True)),
                ('plat_release', models.CharField(max_length=255, null=True)),
                ('hostname', models.CharField(max_length=255)),
                ('local_ip', models.TextField(null=True)),
                ('agent_id', models.CharField(max_length=200)),
                ('last_seen', models.DateTimeField(auto_now=True)),
                ('services', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('public_ip', models.CharField(max_length=255, null=True)),
                ('cpu_load', models.FloatField(null=True)),
                ('total_ram', models.IntegerField(null=True)),
                ('used_ram', models.IntegerField(null=True)),
                ('disks', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('boot_time', models.FloatField(null=True)),
                ('logged_in_username', models.CharField(max_length=200, null=True)),
                ('cpu_info', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('client', models.CharField(max_length=200)),
                ('antivirus', models.CharField(default='n/a', max_length=255)),
                ('site', models.CharField(max_length=150)),
                ('monitoring_type', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=255, null=True)),
                ('mesh_node_id', models.CharField(max_length=255, null=True)),
                ('overdue_email_alert', models.BooleanField(default=False)),
                ('overdue_text_alert', models.BooleanField(default=False)),
                ('overdue_time', models.PositiveIntegerField(default=30)),
                ('uninstall_pending', models.BooleanField(default=False)),
                ('uninstall_inprogress', models.BooleanField(default=False)),
                ('ping_check_interval', models.PositiveIntegerField(default=300)),
                ('needs_reboot', models.BooleanField(default=False)),
                ('managed_by_wsus', models.BooleanField(default=False)),
                ('is_updating', models.BooleanField(default=False)),
                ('choco_installed', models.BooleanField(default=False)),
            ],
        ),
    ]
