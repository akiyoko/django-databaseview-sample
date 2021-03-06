# Generated by Django 3.1.3 on 2020-11-30 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_date', models.DateField(verbose_name='売上日')),
                ('amount', models.PositiveIntegerField(verbose_name='売上金額')),
                ('subject', models.CharField(max_length=255, verbose_name='件名')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
            ],
            options={
                'verbose_name': '売上実績',
                'verbose_name_plural': '売上実績',
                'db_table': 'sales_result',
            },
        ),
        migrations.CreateModel(
            name='SalesTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_month', models.DateField(verbose_name='売上月')),
                ('amount', models.PositiveIntegerField(verbose_name='目標金額')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
            ],
            options={
                'verbose_name': '売上目標',
                'verbose_name_plural': '売上目標',
                'db_table': 'sales_target',
            },
        ),
    ]
