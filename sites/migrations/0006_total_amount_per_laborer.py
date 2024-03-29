# Generated by Django 5.0.2 on 2024-03-24 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0005_attendance_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='total_amount_per_laborer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('Manpower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.manpower')),
            ],
        ),
    ]
