# Generated by Django 4.1.1 on 2022-09-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='date_finish',
            field=models.DateTimeField(db_index=True, verbose_name='Время окончания рассылки'),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='date_start',
            field=models.DateTimeField(db_index=True, verbose_name='Время начала рассылки'),
        ),
    ]
