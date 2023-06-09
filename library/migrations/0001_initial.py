# Generated by Django 4.1.7 on 2023-03-18 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('pages', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cover_type', models.CharField(max_length=50)),
                ('dimensions', models.CharField(max_length=50)),
                ('pub_date', models.DateField()),
                ('poster', models.ImageField(default=False, upload_to='image/')),
            ],
        ),
    ]
