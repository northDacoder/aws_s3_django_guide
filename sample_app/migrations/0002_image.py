# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'blog_images', blank=True)),
                ('caption', models.TextField(blank=True)),
                ('location', models.CharField(max_length=255, blank=True)),
                ('blog', models.ForeignKey(related_name='pictures', to='sample_app.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
