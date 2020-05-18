# Generated by Django 3.0.6 on 2020-05-18 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AddSubject', '0003_marks_subjectcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marks',
            name='subjectcode',
        ),
        migrations.RemoveField(
            model_name='marks',
            name='subcode',
        ),
        migrations.AddField(
            model_name='marks',
            name='subcode',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='AddSubject.Subject'),
        ),
    ]