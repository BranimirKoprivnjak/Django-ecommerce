# Generated by Django 3.2.4 on 2021-06-20 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
        ('shop', '0011_rename_item_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.billingaddress'),
        ),
    ]
