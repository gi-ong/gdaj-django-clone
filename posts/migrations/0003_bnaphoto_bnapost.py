# Generated by Django 3.2.12 on 2022-03-03 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BnAPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=80)),
                ('bna_type', models.CharField(choices=[('치아교정', '치아교정'), ('치아미백', '치아미백')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BnAPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('caption', models.CharField(max_length=80)),
                ('file', models.ImageField(upload_to='bna_photos')),
                ('bna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bna_photos', to='posts.bnapost')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
