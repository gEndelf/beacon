# -*- coding: utf-8 -*-
import github3
from django.conf import settings
from beacon.models import RE_GIT_URL, RE_HTTP_URL


def parse_url(url):
    """
    sample URLs:
    https://github.com/gEndelf/trello-test
    git@github.com:gEndelf/trello-test.git
    git@bitbucket.org:gEndelf/trello-test.git
    """
    matched = RE_GIT_URL.match(url)
    if not matched:
        matched = RE_HTTP_URL.match(url)
        if not matched:
            raise ValueError(
                'url should be valid and contains path to github repo')

    return matched.group('repo_type'), matched.group(
        'organization'), matched.group('repo')


def github_auth():
    return github3.login(settings.GITHUB_USERNAME, settings.GITHUB_PASSWORD)


def get_repo(org, repo):
    repository = github_auth().repository(org, repo)
    return repository


def get_labels(repo):
    existing_labels = [item.name for item in repo.iter_labels()]
    return existing_labels


def create_labels(repo, labels):
    existing_labels = get_labels(repo)

    for label, color in labels.items():
        if label not in existing_labels:
            repo.create_label(label, color)
