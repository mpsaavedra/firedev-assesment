# Generated by Django 3.2.4 on 2021-08-24 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='Name')),
                ('enable', models.BooleanField(default=True, verbose_name='Is Active')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Citites',
            },
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Class name')),
                ('enable', models.BooleanField(default=True, verbose_name='Is Active')),
            ],
            options={
                'verbose_name': 'ClassRoom',
                'verbose_name_plural': 'ClassRooms',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='Name')),
                ('enable', models.BooleanField(default=True, verbose_name='Is active')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='Name')),
                ('email', models.EmailField(max_length=180, verbose_name='Email')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('sex', models.CharField(choices=[('ML', 'Male'), ('FM', 'Female'), ('UK', 'Unnown')], default='UK', max_length=2, verbose_name='Sex')),
                ('classroom', models.ForeignKey(limit_choices_to={'enable': True}, on_delete=django.db.models.deletion.CASCADE, to='classroom.classroom', verbose_name='ClassRoom')),
                ('cob', models.ForeignKey(limit_choices_to={'enable': True}, on_delete=django.db.models.deletion.CASCADE, to='classroom.city', verbose_name='City of Birth')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.AddField(
            model_name='classroom',
            name='teacher',
            field=models.ForeignKey(limit_choices_to={'enable': True}, on_delete=django.db.models.deletion.CASCADE, to='classroom.teacher', verbose_name='Teacher'),
        ),
    ]
