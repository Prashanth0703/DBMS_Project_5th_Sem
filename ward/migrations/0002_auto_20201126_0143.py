# Generated by Django 3.1.3 on 2020-11-25 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nurse', '0001_initial'),
        ('ward', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor_works',
            options={'verbose_name': 'Doctor Working Ward'},
        ),
        migrations.CreateModel(
            name='WARD_MANAGED_BY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MgrNurse_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nurse.nurse_details')),
                ('Ward_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ward.ward_details')),
            ],
            options={
                'verbose_name_plural': 'Ward Managing Nurse',
                'unique_together': {('Ward_ID', 'MgrNurse_ID')},
            },
        ),
        migrations.CreateModel(
            name='NURSE_WORKS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nurse_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nurse.nurse_details')),
                ('Ward_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ward.ward_details')),
            ],
            options={
                'verbose_name': 'Nurse working Ward',
                'unique_together': {('Ward_ID', 'Nurse_ID')},
            },
        ),
    ]