# Generated by Django 4.0.6 on 2022-07-26 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_api', '0006_alter_note_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
