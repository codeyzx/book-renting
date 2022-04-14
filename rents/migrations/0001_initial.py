# Generated by Django 4.0.4 on 2022-04-14 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('BUKU_JONI', 'bukuJoni'), ('BUKU_JERMAN', 'bukuJerman'), ('BUKU_SUBMIT', 'bukuSubmit'), ('BUKU_KAZEHAYA', 'bukuKazehaya')], default='BUKU_JONI', max_length=20)),
                ('photo', models.CharField(choices=[('BUKU_JONI.png', 'bukuJoni.png'), ('BUKU_JERMAN.png', 'bukuJerman.png'), ('BUKU_SUBMIT.png', 'bukuSubmit.png'), ('BUKU_KAZEHAYA.png', 'bukuKazehaya.png')], default='BUKU_JONI.png', max_length=20)),
                ('author', models.CharField(choices=[('JONI', 'joni'), ('JERMAN', 'jerman'), ('SUBMIT', 'submit'), ('KAZEHAYA', 'kazehaya')], default='JONI', max_length=20)),
                ('borrowed_on', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]