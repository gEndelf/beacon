# -*- coding: utf-8 -*-
import logging

from django.core.management.base import BaseCommand

from beacon.service import create_labels, parse_url, get_repo
from beacon.flow import LABELS

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--url', type=str)

    def handle(self, *args, **options):
        url = options.get('url')

        if not url:
            logger.warn('github repo url should be provided')
            return

        try:
            service, org, repo = parse_url(url)
            create_labels(get_repo(org, repo), LABELS)
        except ValueError, e:
            print e.message
