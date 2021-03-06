# Generated by Django 3.2.4 on 2021-06-27 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Axe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('is_completed', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_departement', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Formateur',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('phone_number', models.CharField(max_length=20)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_specialite', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('departement', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stages.departement')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.CharField(max_length=100)),
                ('description_du_stage', models.TextField()),
                ('duree', models.CharField(max_length=100)),
                ('type_de_stage', models.CharField(max_length=100)),
                ('remunere', models.BooleanField()),
                ('nombre_de_stagiaire', models.IntegerField()),
                ('occupe', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('formateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stages.formateur')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Stagiaire',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('phone_number', models.CharField(max_length=20)),
                ('score', models.PositiveBigIntegerField(default=0)),
                ('is_active', models.BooleanField(default=False)),
                ('formateur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stages.formateur')),
                ('specialite', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stages.specialite')),
            ],
        ),
        migrations.CreateModel(
            name='CahierCharge',
            fields=[
                ('stage', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='stages.stage')),
                ('cahierCharge', models.TextField(default='empty...')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('stagiaire', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='stages.stagiaire')),
                ('cv', models.FileField(blank=True, upload_to='cvs')),
                ('rapport', models.FileField(blank=True, upload_to='rapports')),
            ],
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrptionTache', models.TextField()),
                ('is_done', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('axe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stages.axe')),
            ],
        ),
        migrations.AddField(
            model_name='stage',
            name='stagiaire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stages.stagiaire'),
        ),
        migrations.AddField(
            model_name='formateur',
            name='specialite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stages.specialite'),
        ),
        migrations.CreateModel(
            name='Demande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stages.stage')),
                ('stagiaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stages.stagiaire')),
            ],
        ),
        migrations.AddField(
            model_name='axe',
            name='cahierCharge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stages.cahiercharge'),
        ),
    ]
