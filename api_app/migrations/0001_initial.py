# Generated by Django 4.1 on 2022-08-19 01:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('created_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.account')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=600)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.community')),
                ('created_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.account')),
            ],
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('url', models.URLField()),
                ('created_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.account')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.account')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('created_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.account')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.issue')),
                ('tags', models.ManyToManyField(blank=True, to='api_app.tag')),
                ('webpages', models.ManyToManyField(blank=True, to='api_app.webpage')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('created_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.account')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.question')),
                ('webpages', models.ManyToManyField(blank=True, to='api_app.webpage')),
            ],
        ),
        migrations.AddField(
            model_name='community',
            name='tags',
            field=models.ManyToManyField(blank=True, to='api_app.tag'),
        ),
        migrations.AddField(
            model_name='account',
            name='communities',
            field=models.ManyToManyField(blank=True, to='api_app.community'),
        ),
        migrations.AddField(
            model_name='account',
            name='tags',
            field=models.ManyToManyField(blank=True, to='api_app.tag'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='account',
            name='webpages',
            field=models.ManyToManyField(blank=True, to='api_app.webpage'),
        ),
    ]
