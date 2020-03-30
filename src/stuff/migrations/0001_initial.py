# Generated by Django 3.0.4 on 2020-03-30 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('sha256', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('length', models.BigIntegerField(blank=True, null=True)),
                ('full', models.BooleanField(default=False)),
                ('content', models.BinaryField(blank=True, max_length=65536, null=True)),
                ('head', models.BinaryField(blank=True, max_length=256, null=True)),
                ('tail', models.BinaryField(blank=True, max_length=256, null=True)),
                ('preview', models.CharField(blank=True, max_length=64)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
