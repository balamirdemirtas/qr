# Generated by Django 3.0.6 on 2020-05-27 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestOfWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=12)),
                ('info', models.CharField(db_index=True, max_length=58)),
                ('slug', models.SlugField(max_length=30, unique=True)),
                ('image', models.ImageField(upload_to='products/%y/%m/%d')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
    ]
