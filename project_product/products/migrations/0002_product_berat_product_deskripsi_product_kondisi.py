# Generated by Django 4.2.17 on 2024-12-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='berat',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='deskripsi',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='kondisi',
            field=models.CharField(default='baru panen', max_length=50),
        ),
    ]