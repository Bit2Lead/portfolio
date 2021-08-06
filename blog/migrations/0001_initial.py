# Generated by Django 3.2.6 on 2021-08-06 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='blog/images')),
                ('date', models.DateField()),
            ],
        ),
    ]
