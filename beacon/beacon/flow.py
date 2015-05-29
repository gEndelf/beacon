# -*- coding: utf-8 -*-

"""
Flow definition:
predefined issue types:
- type:bug
- type:enhancement

predefined states:
- state:in progress
- state:ready4testing

predefined priority:
- priority:low
- priority:hight
- priority:urgent

"""

LABEL__ISSUE_TYPE = {
    'type:bug': '#fc2929',
    'type:enhancement': '#84b6eb'
}

LABEL__ISSUE_STATE = {
    'state:in progress': '#5319e7',
    'state:ready4testing': '#009800'
}

LABEL__ISSUE_PRIORITY = {
    'priority:low': '#cccccc',
    'priority:hight': '#FF0000',
    'priority:urgent': '#000000'
}

LABELS = dict(dict(LABEL__ISSUE_TYPE, **LABEL__ISSUE_STATE),
              **LABEL__ISSUE_PRIORITY)

BOARD_LISTS = (
    'ideas',
    'backlog',
    'TODO',
    'in progress',
    'ready4testing',
    'done',
)
