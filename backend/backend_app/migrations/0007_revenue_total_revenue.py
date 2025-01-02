# Generated by Django 5.1.4 on 2024-12-28 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0006_expense_product_revenue_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='revenue',
            name='total_revenue',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]