# Generated by Django 2.2.4 on 2019-10-14 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('engine', '0022_auto_20191004_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('task_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key='True', serialize=False, to='engine.Task')),
                ('instruction_text', models.CharField(max_length=256, null='True')),
            ],
        ),
    ]
