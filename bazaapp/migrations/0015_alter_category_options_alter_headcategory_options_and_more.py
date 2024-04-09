# Generated by Django 4.2.11 on 2024-04-09 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaapp', '0014_status_headcategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Xizmat turi', 'verbose_name_plural': 'Xizmat turlari'},
        ),
        migrations.AlterModelOptions(
            name='headcategory',
            options={'verbose_name': 'Departament', 'verbose_name_plural': 'Departamentlar'},
        ),
        migrations.AddField(
            model_name='status',
            name='deadline',
            field=models.CharField(blank=True, max_length=15, verbose_name='Deadline Vaqti'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, max_length=80, null=True, unique=True, verbose_name='Xizmat turlari'),
        ),
        migrations.AlterField(
            model_name='headcategory',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Departament'),
        ),
    ]