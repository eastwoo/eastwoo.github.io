#!/usr/bin/env python
import sys
import datetime
import re

# define the blog title is sys.argv[1]
blog_title = sys.argv[1]
blog_file = re.sub(r' ', r'-', blog_title)

day_time = datetime.datetime.now().strftime("%F %X").split()
Today = day_time[0]
create_time = day_time[1]

init_info = """---
layout: post
title:  "{}"
date:  {}
---
""".format(blog_title, ' '.join(day_time))


print '{} {}'.format(Today, create_time)
new_blog_filename = '{}-{}.markdown'.format(Today, blog_file)
print new_blog_filename

def init_blog(filename, content):
    os.chdir('_posts')
    fobj = open(filename, 'w')
    fobj.write(content)
    fobj.close()


def main():
    init_blog(new_blog_filename, init_info)

if __name__ == '__main__':
    main()
