# Generated by Django 3.1.7 on 2021-03-02 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbpost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodclass3',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='bbpost.bloodclass2'),
        ),
    ]