# Generated by Django 5.0.2 on 2024-03-16 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_tool_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='present_or_absent',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Present', max_length=10),
            preserve_default=False,
        ),
    ]