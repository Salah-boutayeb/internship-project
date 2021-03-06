# Generated by Django 3.2.4 on 2021-06-27 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileStagiaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('avatar', models.ImageField(default='user.png', upload_to='avatars')),
                ('linkedin', models.URLField(blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stages.stagiaire')),
            ],
        ),
    ]
