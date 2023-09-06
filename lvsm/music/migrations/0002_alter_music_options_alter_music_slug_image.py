# Generated by Django 4.2.4 on 2023-09-06 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='music',
            options={'ordering': ['-time_create', 'title'], 'verbose_name': 'Musician'},
        ),
        migrations.AlterField(
            model_name='music',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='URL'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='music.music')),
            ],
            options={
                'ordering': ['music'],
            },
        ),
    ]
