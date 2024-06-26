# Generated by Django 5.0.4 on 2024-04-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_created_on_blog_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.CharField(blank=True, help_text='Enter tags separated by commas', max_length=255),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_on',
            field=models.DateField(auto_now=True),
        ),
    ]
