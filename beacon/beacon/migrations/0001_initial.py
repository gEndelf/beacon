# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('repo_type', models.CharField(default=b'github', max_length=15, choices=[(b'github', b'github'), (b'bitbucket', b'bitbucket')])),
                ('organization', models.CharField(max_length=70)),
                ('repo', models.CharField(max_length=70)),
                ('title', models.CharField(max_length=70)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='repo',
            unique_together=set([('repo_type', 'organization', 'repo')]),
        ),
    ]
