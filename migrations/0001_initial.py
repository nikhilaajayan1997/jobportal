# Generated by Django 4.0.4 on 2022-05-19 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=150)),
                ('company_name', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=120)),
                ('salary', models.PositiveIntegerField(null=True)),
                ('experience', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
