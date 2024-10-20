# Generated by Django 5.1.2 on 2024-10-19 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('Question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
            ],
        ),
    ]
