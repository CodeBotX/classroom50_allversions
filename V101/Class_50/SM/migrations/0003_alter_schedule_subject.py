# Generated by Django 4.2.6 on 2024-04-06 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SM', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='subject',
            field=models.ForeignKey(default='Trống', on_delete=django.db.models.deletion.CASCADE, to='SM.subject'),
        ),
    ]