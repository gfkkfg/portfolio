# Generated by Django 5.2.2 on 2025-06-22 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('web', 'Web'), ('android', 'Android'), ('ai', 'AI'), ('iot', 'IoT'), ('others', 'Others')], default='others', max_length=50),
        ),
    ]
