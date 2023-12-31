# Generated by Django 4.2.8 on 2023-12-18 13:38

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
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_address', models.CharField(blank=True, max_length=254, null=True, verbose_name='Wallet Address')),
                ('wallet_balance', models.PositiveIntegerField(default=0)),
                ('private_key', models.TextField(blank=True, null=True, verbose_name='Rrivate Key')),
                ('public_key', models.TextField(blank=True, null=True, verbose_name='Public Key')),
                ('mnemonic_phrase', models.TextField(blank=True, null=True, verbose_name='Mnemonic Phrase')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Name of the analysis')),
                ('parameter', models.TextField(verbose_name='Name of the parameter')),
                ('parameter_value', models.TextField(verbose_name='Parameter value')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testcards', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
