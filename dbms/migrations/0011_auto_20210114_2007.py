# Generated by Django 3.0.7 on 2021-01-14 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dbms', '0010_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=15, null=True)),
                ('phonenumber', models.IntegerField(null=True)),
                ('address', models.CharField(default='', max_length=15, null=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=15, null=True)),
                ('phonenumber', models.IntegerField(null=True)),
                ('address', models.CharField(default='', max_length=15, null=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('is_teacher', 'can view marks'),),
            },
        ),
        migrations.RemoveField(
            model_name='geo_tagging',
            name='user',
        ),
        migrations.DeleteModel(
            name='FUND_DETAILS',
        ),
        migrations.DeleteModel(
            name='GEO_TAGGING',
        ),
    ]