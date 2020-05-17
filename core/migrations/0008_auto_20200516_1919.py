# Generated by Django 3.0.5 on 2020-05-16 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200516_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitacaomatricula',
            name='disciplinaofertada',
        ),
        migrations.AddField(
            model_name='solicitacaomatricula',
            name='curso',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='core.Curso'),
        ),
    ]
