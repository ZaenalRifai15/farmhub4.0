# Generated by Django 4.2.17 on 2024-12-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_kondisi'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='kategori',
            field=models.CharField(choices=[('Sayuran', 'sayuran'), ('Buah', 'buah'), ('Hasil Ternak', 'hasil ternak')], default='Hasil tani', max_length=50),
        ),
    ]
