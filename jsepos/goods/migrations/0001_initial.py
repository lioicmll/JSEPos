# Generated by Django 2.2 on 2019-04-24 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=30)),
                ('bar_code', models.BigIntegerField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
