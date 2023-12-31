# Generated by Django 4.2.4 on 2023-08-30 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_album_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='songinalbum',
            options={'ordering': ('number',)},
        ),
        migrations.RemoveField(
            model_name='album',
            name='name',
        ),
        migrations.AlterField(
            model_name='songinalbum',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='api.song'),
        ),
    ]
