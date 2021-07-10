# Generated by Django 3.0.7 on 2021-07-10 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dbms', '0025_auto_20210710_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default=None, max_length=1000)),
                ('website', models.CharField(default=None, max_length=1000)),
                ('role', models.CharField(default=None, max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
