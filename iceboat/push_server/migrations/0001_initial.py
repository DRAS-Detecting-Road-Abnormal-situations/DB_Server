# Generated by Django 3.1.3 on 2020-11-18 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=False, max_length=10)),
                ('image', models.ImageField(default=False, upload_to='situation_image')),
            ],
        ),
    ]