# Generated by Django 4.2.2 on 2023-07-22 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('device_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('encrypted_samples', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SignatureSample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature_image', models.ImageField(upload_to='signature_samples/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signatures.user')),
            ],
        ),
    ]
