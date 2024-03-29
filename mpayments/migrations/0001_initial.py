# Generated by Django 4.2 on 2024-01-30 12:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MpesaTransaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=30)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('receipt_number', models.CharField(blank=True, max_length=30, null=True)),
                ('merchant_request_id', models.CharField(max_length=30)),
                ('checkout_request_id', models.CharField(max_length=100)),
                ('result_code', models.CharField(blank=True, max_length=20, null=True)),
                ('result_description', models.TextField(blank=True, null=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('is_successful', models.BooleanField(default=False)),
                ('is_utilised', models.BooleanField(default=False)),
                ('transaction_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
