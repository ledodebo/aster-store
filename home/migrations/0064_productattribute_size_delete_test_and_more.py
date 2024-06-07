# Generated by Django 4.2.7 on 2024-05-27 21:18

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0063_delete_test_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to='product_imgs/')),
            ],
            options={
                'verbose_name_plural': '7. ProductAttributes',
            },
        ),
        migrations.CreateModel(
            name='size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(default=100, max_length=20)),
            ],
        ),
       
        migrations.AlterField(
            model_name='product',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=75, scale=None, size=[4578, 5723], upload_to='uploads/product'),
        ),
        migrations.AddField(
            model_name='productattribute',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product'),
        ),
        migrations.AddField(
            model_name='productattribute',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.size'),
        ),
    ]
