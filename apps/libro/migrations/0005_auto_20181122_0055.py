# Generated by Django 2.0.6 on 2018-11-22 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0004_auto_20181122_0053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='autor_id',
        ),
        migrations.AddField(
            model_name='libro',
            name='autor_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='libro.Autor'),
            preserve_default=False,
        ),
    ]
