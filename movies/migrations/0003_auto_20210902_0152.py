# Generated by Django 2.2.1 on 2021-09-01 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20210901_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cast_members', models.TextField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movies.Movie')),
            ],
        ),
    ]
