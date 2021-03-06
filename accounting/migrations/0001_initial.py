# Generated by Django 3.2 on 2021-04-12 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Account Name')),
                ('balance_type', models.CharField(choices=[('credit', 'Credit'), ('debit', 'Debit')], max_length=6, verbose_name='Account Balance Type')),
            ],
        ),
        migrations.CreateModel(
            name='SubAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='Account Code')),
                ('name', models.CharField(max_length=100, verbose_name='Sub-Account Name')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_account', to='accounting.account')),
            ],
        ),
    ]
