---
layout: post
title:  "setup-ssh-client-authention-orders"
date:  2016-10-27 13:03:58
---

# setup ssh-client authentication orders

modify /etc/ssh/ssh_config
    Host *
        GSSAPIAuthentication yes
        PreferredAuthentications publickey,password,keyboard-interactive
