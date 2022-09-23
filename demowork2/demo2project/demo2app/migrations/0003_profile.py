# Generated by Django 3.2.15 on 2022-08-28 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo2app', '0002_rename_image_destinations_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('pic', models.ImageField(upload_to='pics')),
                ('disc', models.TextField()),
            ],
        ),
    ]