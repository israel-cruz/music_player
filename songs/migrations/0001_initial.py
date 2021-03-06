# Generated by Django 3.2.6 on 2021-08-14 00:58

from django.db import migrations, models
import django.db.models.deletion
import songs.audio_tools


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('artist', models.CharField(max_length=256)),
                ('time_length', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('audio_file', models.FileField(upload_to='songs/', validators=[songs.audio_tools.validate_is_audio])),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='songs.album')),
            ],
        ),
    ]
