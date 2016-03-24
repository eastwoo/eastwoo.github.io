---
layout: post
title:  "github https credential"
date:   2016-03-23 16:12:22
---

# setup the github https credentials

## you just need to execute two commands to finish  this task

        # Set git to use the credential memory cache
        git config --global credential.helper cache

        # Set the cache to timeout after 1 hour (setting is in seconds)
        git config --global credential.helper 'cache --timeout=3600'

## you can get help from here:
[helpgithub](https://help.github.com/articles/caching-your-github-password-in-git/)
