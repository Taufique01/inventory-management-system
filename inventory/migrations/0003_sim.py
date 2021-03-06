# Generated by Django 3.2 on 2021-04-30 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_stockin_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('retail_price', models.FloatField(default=0)),
                ('consumer_price', models.FloatField(default=0)),
                ('available_item', models.FloatField(default=0)),
                ('purchased_item', models.FloatField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
