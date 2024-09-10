# Generated by Django 4.0.5 on 2022-07-27 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('coach', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pref_name', models.CharField(max_length=20, null=True)),
                ('student_phone', models.CharField(max_length=20, null=True)),
                ('student_email', models.CharField(max_length=100, null=True)),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.roster')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.team')),
            ],
        ),
        migrations.AddField(
            model_name='roster',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.team'),
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_name', models.CharField(max_length=100)),
                ('donor_email', models.CharField(max_length=100)),
                ('donor_phone', models.CharField(max_length=20)),
                ('donor_address', models.CharField(max_length=200)),
                ('donor_city', models.CharField(max_length=100)),
                ('donor_zip', models.CharField(max_length=10)),
                ('donor_state', models.CharField(max_length=100)),
                ('donor_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.roster')),
            ],
        ),
    ]
