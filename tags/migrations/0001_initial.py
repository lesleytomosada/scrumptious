# Generated by Django 4.0.3 on 2022-08-25 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('recipes', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tags', to='recipes.recipe')),
            ],
        ),
    ]
