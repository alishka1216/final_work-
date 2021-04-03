# Generated by Django 2.2 on 2021-04-03 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20210403_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question_poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('publish_date', models.DateTimeField(blank=True, null=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Question')),
            ],
        ),
    ]