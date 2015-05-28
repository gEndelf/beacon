import re

from django.db import models

RE_GIT_URL = re.compile(
    'git@(?P<repo_type>(github|bitbucket))\.com:(?P<organization>\w+)/(?P<repo>[a-zA-Z0-9\-]+)\.git')
RE_HTTP_URL = re.compile(
    'https://(?P<repo_type>(github|bitbucket))\.com/(?P<organization>\w+)/(?P<repo>[a-zA-Z0-9\-]+)/?.*')


class Repo(models.Model):
    GITHUB = 'github'
    BITBUCKET = 'bitbucket'

    REPO_TYPE = [
        (GITHUB, 'github'),
        (BITBUCKET, 'bitbucket'),
    ]

    repo_type = models.CharField(max_length=15,
                                 choices=REPO_TYPE,
                                 default=GITHUB)
    organization = models.CharField(max_length=70)
    repo = models.CharField(max_length=70)
    title = models.CharField(max_length=70)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        unique_together = ('repo_type', 'organization', 'repo')

    def __unicode__(self):
        return self.name
