# Generated by Django 4.2.2 on 2023-06-24 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SwapOffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isAccepted', models.BooleanField(default=False)),
                ('token_to_recieve', models.CharField(max_length=30)),
                ('number_of_token_to_recieve', models.CharField(max_length=30)),
                ('token_to_swap', models.CharField(max_length=30)),
                ('number_of_token_to_swap', models.CharField(max_length=30)),
                ('offer_accepter', models.CharField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('offer_maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
