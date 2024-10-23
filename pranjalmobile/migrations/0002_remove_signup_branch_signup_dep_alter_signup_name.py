# Generated by Django 5.1.2 on 2024-10-22 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pranjalmobile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='branch',
        ),
        migrations.AddField(
            model_name='signup',
            name='dep',
            field=models.CharField(choices=[('IT', 'IT'), ('NON-IT', 'NON-IT')], default='test', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='signup',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
