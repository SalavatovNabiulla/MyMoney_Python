# Generated by Django 4.0.3 on 2022-12-23 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_wallets_balances_wallet_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='cost_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='revenue_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='transactions',
            name='cost_item_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='core.cost_items'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='revenue_item_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='core.revenue_items'),
        ),
    ]
