#!/usr/bin/env python
import sys
import datetime
import re
import os

# define the blog title is sys.argv[1]
if len(sys.argv) == 1:
    print 'Usage: ./$script_name new_blog_name'
    sys.exit()
blog_title = sys.argv[1]
blog_file = re.sub(r' ', r'-', blog_title)

# create the time format is ['2016-03-24', '16:13:26']
day_time = datetime.datetime.now().strftime("%F %X").split()
Today = day_time[0]

# we need setup the date to yesterday to fix the list in the eastwoo.github.io
Yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%F')
create_time = day_time[1]

# the info should be put into the blog first
init_info = """---
layout: post
title:  "{}"
date:  {}
---
""".format(blog_title, Yesterday + " " +  create_time)

# the blog filename
new_blog_filename = '{0}-{1}.markdown'.format(Today, blog_file)

def init_blog(filename, content):
    os.chdir('_posts')
    fobj = open(filename, 'w')
    fobj.write(content)
    fobj.close()

if __name__ == '__main__':
    init_blog(new_blog_filename, init_info)
