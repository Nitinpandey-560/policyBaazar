# Generated by Django 2.1.7 on 2021-06-28 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance_Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_name', models.CharField(max_length=100)),
                ('sum_assured', models.IntegerField()),
                ('premium', models.IntegerField()),
                ('tenure', models.IntegerField()),
                ('creation_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Main_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(max_length=50)),
                ('catdesc', models.CharField(max_length=200)),
                ('cat_image', models.ImageField(blank=True, upload_to='cat_image')),
                ('creation_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Main_SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_catname', models.CharField(max_length=50)),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('catid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Main_Category')),
            ],
        ),
        migrations.AddField(
            model_name='insurance_policy',
            name='catid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Main_Category'),
        ),
        migrations.AddField(
            model_name='insurance_policy',
            name='sub_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Main_SubCategory'),
        ),
    ]