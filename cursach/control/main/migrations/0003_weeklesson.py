# Generated by Django 5.0.3 on 2024-05-17 17:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='weeklesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lessonday', models.CharField(max_length=250, verbose_name='Учебный день')),
                ('group_1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Класс_1', to='main.group')),
                ('group_2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Класс_2', to='main.group')),
                ('group_3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Класс_3', to='main.group')),
                ('group_4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Класс_4', to='main.group')),
                ('lesson_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Урок_1', to='main.lesson')),
                ('lesson_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Урок_2', to='main.lesson')),
                ('lesson_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Урок_3', to='main.lesson')),
                ('lesson_4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Урок_4', to='main.lesson')),
            ],
        ),
    ]
