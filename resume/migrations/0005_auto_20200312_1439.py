# Generated by Django 3.0.3 on 2020-03-12 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20200310_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='organization_name',
            new_name='company_name',
        ),
        migrations.AddField(
            model_name='experience',
            name='description',
            field=models.CharField(max_length=70, null=True, verbose_name='Description'),
        ),
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