# -*- coding: utf-8 -*-

from docutils.core import publish_parts

from recommonmark.parser import CommonMarkParser


def test_basic_parser():
    source = '# Header'

    ret = publish_parts(
        source=source,
        writer_name='html',
        parser=CommonMarkParser()
    )

    assert ret['title'] == 'Header'
