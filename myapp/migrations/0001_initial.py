# Generated by Django 3.1.2 on 2021-02-20 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('pwd', models.CharField(max_length=50)),
                ('pic', models.ImageField(upload_to='')),
            ],
        ),
    ]