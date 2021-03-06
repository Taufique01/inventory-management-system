# Generated by Django 3.2 on 2021-05-01 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_sim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit_type',
            field=models.CharField(blank=True, choices=[('Quantity', 'Quantity'), ('Gram', 'Gram'), ('Litre', 'Litre'), ('Kilogram', 'Kilogram')], default='Quantity', max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='SimSeLL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sim_number', models.CharField(max_length=15)),
                ('notes', models.CharField(max_length=500)),
                ('paid_by', models.CharField(choices=[('customer', 'CUSTOMER'), ('company', 'COMPANY')], max_length=15)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sim_sell', to='inventory.customer')),
                ('sim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sim_sell', to='inventory.sim')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
