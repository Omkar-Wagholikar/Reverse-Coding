# Generated by Django 4.1.1 on 2023-05-07 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_RC', '0008_profile_correctanswers'),
    ]

    operations = [
        migrations.AddField(
            model_name='easyquestion',
            name='question_id',
            field=models.IntegerField(default=0),
        ),
    ]
