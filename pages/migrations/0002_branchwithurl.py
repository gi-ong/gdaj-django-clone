# Generated by Django 3.2.12 on 2022-03-16 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchWithUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('url_name', models.CharField(max_length=20)),
                ('branch_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='pages.branch')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
