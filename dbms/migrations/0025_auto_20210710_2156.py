# Generated by Django 3.0.7 on 2021-07-10 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbms', '0024_results'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='img',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dbms.Exam'),
        ),
    ]
