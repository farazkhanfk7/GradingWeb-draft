# Generated by Django 2.2.12 on 2020-04-23 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='desc',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
