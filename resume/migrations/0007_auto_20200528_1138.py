# Generated by Django 3.0.3 on 2020-05-28 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_auto_20200410_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='resume_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.Resume'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='resume_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.Resume'),
        ),
    ]
