# Generated by Django 5.0.6 on 2024-06-13 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_remove_recipe_image_path_remove_recipe_pdf_path_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image_data',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='pdf_data',
            field=models.FileField(blank=True, upload_to='pdf/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='video_data',
            field=models.FileField(blank=True, upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='video_stream_data',
            field=models.FileField(blank=True, upload_to='videos/stream/'),
        ),
    ]
