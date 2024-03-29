#coding:utf-8

"""
ID:          NOT YET ASSIGNED.
ISSUE:       NOT YET ASSIGNED.
TITLE:       NOT YET ASSIGNED.
DESCRIPTION: STUB. TO BE FILLED LATER.
NOTES:
"""

import pytest
from firebird.qa import *

db = db_factory()

act = python_act('db')

@pytest.mark.version('>=3.0')
def test_1(act: Action, capsys):
    act.expected_stdout = ''
    act.stdout = capsys.readouterr().out
    assert act.clean_stdout == act.clean_expected_stdout
