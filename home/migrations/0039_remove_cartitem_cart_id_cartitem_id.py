# Generated by Django 4.2.7 on 2024-04-07 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_order_iteams'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart_id',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
