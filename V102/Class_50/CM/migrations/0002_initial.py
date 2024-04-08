# Generated by Django 4.2.7 on 2024-04-06 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SM', '0001_initial'),
        ('CM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='SM.classroom'),
        ),
        migrations.AddField(
            model_name='seat',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seat', to='SM.student'),
        ),
        migrations.AddField(
            model_name='lessons',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SM.classroom'),
        ),
        migrations.AddField(
            model_name='lessons',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SM.subject'),
        ),
    ]
