# encoding=utf-8
import os
import re
from datetime import datetime

HEADER_TEMPLE = """---
title: {title}
date: {date}
tags: {tags}
categories: {category}
---
# {title}
"""


class Header(object):
    def __init__(self, title, date, tag_string=None, category=None):
        self.title = title
        self.date = date
        self.tag_string = tag_string
        self.category = category

    def __str__(self):
        return HEADER_TEMPLE.format(title=self.title, date=self.date,
                                    tags=self.format_tags(),
                                    category=self.category
                                    )

    def format_tags(self):
        tags_string = ""
        for tag in re.split(r'\W+', self.tag_string):
            tags_string += "\n\t- {tag}".format(tag=tag)
        return tags_string


class Markdown(object):
    def __init__(self, path, tag_string=None, category=None):
        self.path = path
        self.tag_string = tag_string
        self.category = category
        self._header = None

    @property
    def header(self):
        if not self._header:
            title = os.path.basename(os.path.splitext(self.path)[0])
            date = datetime.fromtimestamp(os.path.getctime(self.path)).strftime('%Y-%m-%d %H:%M:%S')
            self._header = Header(title, date, self.tag_string, self.category)
        return self._header


if __name__ == '__main__':
    fname = input(u"file name: ")
    tags = input("tags: ")
    category = input("category: ")
    md = Markdown(fname)
    print(str(md.header))
    # with open(fname, 'wb') as f:
    #     f.write(str(md.header))
